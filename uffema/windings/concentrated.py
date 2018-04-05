#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# ==========================================================================
# Copyright (C) 2016 Dr. Alejandro Pina Ortega
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==========================================================================

import scipy.interpolate as si
from scipy.fftpack import fft
from uffema.materials import Material
from uffema.slots import Type0
from uffema.misc import *
from winding import Winding


class Concentrated(Winding):
    def __init__(self,  phases=3, layers=2, conn='wye', C=[],
                 mat = Material(), series=1, parallel=1, coilTurns=10, wih=1,
                 condDiam=1e-3, coilPitch=1,
                 Ns=12, slot=Type0(), iSr=22.95e-3, Sl=30e-3):
        lsw = Sl
        slotCenter = slot.get_slot_center()
        lew = (PI ** 2) * coilPitch * (2.0 / Ns) * (iSr + slotCenter)
        Winding.__init__( self, phases, layers, conn, coilTurns*C, mat, series,
                          parallel, coilTurns, wih, condDiam, coilPitch,
                          lsw, lew, slot)
        # For right-left coil sides, there is phase separator in
        # between (or air), it is assumed 1mm
        self._ph_sep = 1e-3
        # As for end winding length before bending it is assumed 1mm
        self._EWl_bb = 1e-3



    def turns_density(self, m=3, Ns=12, psi=np.linspace(0, 2*PI, 360)):
        """Get turns density for non-overlaping side-by-side coils

        Compute turns density according to Krause in 'Analysis of electric
        machinery and drive systems' 2013 and connection matrix from Pina Ortega
        in 'Modeling and analysis of asymmetries in permanent magnet synchronous
        machines' 2016

        Args:
            m:         Number of phases
            Ns:        Slot number
            psi:       Spatial position

        Returns:
            td:        Turns density
        """
        td = np.zeros((m, Ns+1))
        for i in range(0,Ns):
            td[0,i+1] = td[0,i] + self._C[0,i] + self._C[3,i]
            td[1,i+1] = td[1,i] + self._C[1,i] + self._C[4,i]
            td[2,i+1] = td[2,i] + self._C[2,i] + self._C[5,i]
        td_unshift_intpl = si.interp1d(range(0, Ns+1), td , kind='nearest')
        td_unshift = td_unshift_intpl(np.linspace(0, Ns, len(psi)))
        td_shift = np.zeros_like(td_unshift)
        td_shift[0] = td_unshift[0,:] - np.average(td_unshift[0,:])
        td_shift[1] = td_unshift[1, :] - np.average(td_unshift[1, :])
        td_shift[2] = td_unshift[2, :] - np.average(td_unshift[2, :])

        return td_shift

    def winding_function(self, m=3, Ns=12, pp=4, psi=np.linspace(0, 2*PI, 360)):
        """Get winding function for non-overlaping side-by-side coils

        Compute winding function according to Krause in 'Analysis of electric
        machinery and drive systems' 2013

        Args:
            m:         Number of phases
            Ns:        Slot number
            pp:        Pole per pair
            psi:       Spatial position

        Returns:
            wf:         Winding function
        """
        td = self.turns_density(m, Ns, psi)
        pole_pitch_points = (np.rint(len(psi)/(2*pp))).astype(int)
        wf = np.zeros_like(td)
        #wf0 = np.trapz(td[:,0:pole_pitch_points], dx=PI/180, axis=1)
        #wf[0,1:] = wf0[0] - sp.integrate.cumtrapz(td[0,:], dx=PI/180)
        #wf[1,1:] = wf0[1] - sp.integrate.cumtrapz(td[1, :], dx=PI / 180)
        #wf[2,1:] = wf0[2] - sp.integrate.cumtrapz(td[2, :], dx=PI / 180)
        wf[0] = -td[0, :]
        wf[1] = -td[1, :]
        wf[2] = -td[2, :]
        #wf[0, 0] = wf[0, -1]
        #wf[1, 0] = wf[1, -1]
        #wf[2, 0] = wf[2, -1]

        return wf

    def winding_harmonics(self, m=3, Ns=12, pp=4, psi=np.linspace(0, 2*PI, 360)):
        """Get winding harmonics for non-overlaping side-by-side coils

        Compute winding harmonics according to Ponomarev et al. 'Effect of Slot-and-Pole
        Combination on the Leakage Inductance and the Performance of Tooth-Coil
        Permanent-Magnet Synchronous Machines' in IEEE Transactions on Industrial
        Electronics (2013)

        Args:
            m:         Number of phases
            Ns:        Slot number
            pp:        Pole per pair
            psi:       Spatial position

        Returns:
            wh:         Winding harmonics
        """
        td = (self.turns_density(m, Ns, psi))/self._Cturns
        N = len(td[0])
        N_half = (np.rint(N/2.0)).astype(int)
        td_fft = fft(td[0])
        wh = (2.0 / N)*np.abs(td_fft[0:N_half])
        return wh

    def winding_factors(self, m=3, Ns=12, pp=4, psi=np.linspace(0, 2*PI, 360)):
        """Get winding factors for non-overlaping side-by-side coils

        Compute winding factors according to Ponomarev et al. 'Effect of Slot-and-Pole
        Combination on the Leakage Inductance and the Performance of Tooth-Coil
        Permanent-Magnet Synchronous Machines' in IEEE Transactions on Industrial
        Electronics (2013)

        Args:
            m:         Number of phases
            Ns:        Slot number
            pp:        Pole per pair
            psi:       Spatial position

        Returns:
            kw_v:       Winding factors
        """
        # the larger psi, the smaller the error in winding factors
        td = self.winding_harmonics(m, Ns, pp, psi=np.linspace(0, 2*PI, 5760))
        v = np.linspace(1, len(td)-1, len(td)-1 )
        kw_v = 0.5*td[1:] * v * PI * m / Ns
        return kw_v

    def end_winding_permeance(self, Sb=10e-3):
        """Get end winding leakage for non-overlaping side-by-side coils

        Compute end winding leakage according to Paul et al. 'Drive response modeling of dual
        wound surface permanent magnet machines' in IEMDC (2017) and Cassimere et al.
        'Analytical Design Model for Surface-Mounted Permanent-Magnet Synchronous Machines'
         in IEEE Transactions on Energy Conversion (2009)

        Args:
            Sb:         Stator back iron thickness

        Returns:
            Perm_ew:    Permeance end winding
        """
        st = self._slot.get_slot_type()
        if st == 0:
            cw = 0.5*((self._slot._w0 + self._slot._w1)/2.0 - self._ph_sep)
            lew = self._EWl / 2.0
            lbb = self._EWl_bb
            h2 = self._slot._h2
            aux = h2 - cw
            Perm_1 = (MU0 * lew / (cw**2 * h2**2))*( 0.03125*cw**4 + 0.0625*(cw**3)*aux +
                                                   0.015625*(cw**2)*(aux**2) - 0.015625*cw*(aux**3) +
                                                   7.8125e-3*(aux**4)*np.log(1+(2*cw)/aux))
            Perm_2 = (MU0 * lew ) * ( (lbb+2*cw)/Sb + (3*h2+Sb)/(4*cw) + (lbb+2*cw)/h2 )**(-1)
            Perm_ew = 2*(Perm_1 + Perm_2)
            return  Perm_ew
        else:
            pass


    def slot_permeances(self):
        """Get slot permeances for non-overlaping side-by-side coils

        Compute slot permeances according to Paul et al. 'Drive response modeling of dual
        wound surface permanent magnet machines' in IEMDC (2017) and Lipo in 'Introduction
        to ac machine design' 2011

        Args:

        Returns:
            P0:     Permeance slot opening region
            P1:     Permeance tooth-tip-wedge region
            P2:     Permenace wedge-coil region
            P3:     Permeance coil region
        """
        st = self._slot.get_slot_type()
        P0 = 0.0
        P1 = 0.0
        P2 = 0.0
        P3 = 0.0
        if st == 0:
            P0 = MU0 * self._slot._h0 / self._slot._w0
            P1 = (( MU0 * self._slot._h1 / (self._slot._w1 - self._slot._w0) ) *
                  np.log(self._slot._w1 - self._slot._w0))
            P2 = 0.0    # This region is not accounted for in type 0
            c1 = np.abs(self._slot._w2 - self._ph_sep) / 2.0
            c2 = self._slot._w2
            m1 = -(self._slot._w2 - self._slot._w1) / (2*self._slot._h2)
            m2 = -(self._slot._w2 - self._slot._w1) / self._slot._h2
            d3 = self._slot._h2
            aux1 = ( 0.5*d3**2 - d3 * c2 / m2 +
                     (c2**2 * np.log(c2 + d3 * m2) / (m2**2) -
                      (c2**2 * np.log(c2) / (m2**2) ) ) )
            aux2 = ( (2 * c1 * m2 - c2 * m1)**2) / (m2**3)
            aux3 = ( (d3 ** 4 * m1 ** 2 / (4 * m2)) +
                     (d3 ** 3 * m1 * (4 * c1 * m2 - c2 * m1)) / (3 * m2**2 ) )
            P3 = ( ( MU0 /((d3**2) * (m1 * d3 + 2 * c1)**2) ) *
                   (aux3 + aux2 * aux1) )
        else:
            pass

        return P0, P1, P2, P3