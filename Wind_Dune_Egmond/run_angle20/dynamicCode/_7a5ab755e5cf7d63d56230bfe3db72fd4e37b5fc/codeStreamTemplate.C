/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Copyright (C) YEAR OpenFOAM Foundation
     \\/     M anipulation  |
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

Description
    Template for use with codeStream.

\*---------------------------------------------------------------------------*/

#include "dictionary.H"
#include "Ostream.H"
#include "Pstream.H"
#include "unitConversion.H"

//{{{ begin codeInclude
#line 75 "/scratch/Saeb_OpenFoam/Wind_Dune_cyc_snappy_6April2023/run_angle20/processor0/0/nut/boundaryField/ground/#codeStream"
#include "fvCFD.H"
			#include <math.h>   ///////////
			#include <cmath>    //////////
//}}} end codeInclude

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

extern "C"
{
    void codeStream_7a5ab755e5cf7d63d56230bfe3db72fd4e37b5fc
    (
        Ostream& os,
        const dictionary& dict
    )
    {
//{{{ begin code
        #line 91 "/scratch/Saeb_OpenFoam/Wind_Dune_cyc_snappy_6April2023/run_angle20/processor0/0/nut/boundaryField/ground/#codeStream"
const IOdictionary& d = static_cast<const IOdictionary&>
			(
				dict.parent().parent()
			);
			const fvMesh& mesh = refCast<const fvMesh>(d.db());
			const label id = mesh.boundary().findPatchID("ground");
			const fvPatch& patch = mesh.boundary()[id];
			
			scalarField Ks_fun(patch.size(), 0.);

			
			//vectorField U(patch.size(), vector(0, 0, 0));
			
			//const scalar  pi = constant::mathematical::pi;
			//const scalar  U_0 = 2.; //maximum velocity
			//const scalar  p_ctr = 8.; //patch center     
			//const scalar  p_r = 8.; //patch radius
			
			double L1_band_front_beach = 50;
			double L1_band_front_foredune = 75;
            double L1_band_top_foredune = 125;
			double L1_band_back_foredune = 150;
			
            if (Pstream::master()) 
			{			
			std::ofstream write_L1_band;
	        write_L1_band.open("write_L1_band", std::ofstream::out | std::ofstream::app);  
	        write_L1_band.precision(20);
	        write_L1_band <<  "L1_band_front_beach: " << L1_band_front_beach << "\n" << "L1_band_front_foredune: " <<  L1_band_front_foredune  << "\n" << "L1_band_top_foredune: " <<  L1_band_top_foredune  << "\n" << "L1_band_back_foredune: " <<  L1_band_back_foredune  << "\n";
	        write_L1_band.close();
			}
			
			
			  forAll(Ks_fun, i)   // eqiuvalent to for (int i=0; patch.size()<i; i++)   
			{
				//const scalar y = patch.Cf()[i][1];
				
				//double aa1 = ((y+(5.000000e-04)) / (5.000000e-04)) +10.;
				
				//const double y = patch.Cf()[i][1];
				const double x = patch.Cf()[i][0];

				
				//double y_01 = -10;
				//double y_elevation_from0 = y + (-y_01);
				//double y_elevation_from0 = y + (-1*$y_0);

								
				//double aa1 = 12.+ y;   //( (5.000000e-04+ y) / (5.000000e-04))+10.;    ;


				//double u_x =  log(aa1));
				
				//double aa =log(10.1);
				
				//double aa2 =log(aa1);
				
				// U[i] = vector(((8.500000e-01) / (4.200000e-01))* (log((y+(5.000000e-04)) / (5.000000e-04))), 0., 0.);   // vector(($u_star/4.200000e-01)*log((y+5.000000e-04)/5.000000e-04), 0., 0.);  // vector (20, 0 ,0);   

                // U[i] = vector(((8.500000e-01) / (4.200000e-01) )*($a*fabs((pow(y,3))))+($b*(pow(y,2))), 0., 0.);

				// U[i] = vector(2, 0., 0.);
				


				//double Ks_fun_sand = 0.05;
				//double Ks_fun_Marram_grass = 0.24;
				//double Ks_fun_Marram_grass_and_sand = 0.19;
				
				//double Ks_fun1 = 0.00001;
				
				double Ks_fun1;
								
				if (x <= 50)  {


				Ks_fun1=5.000000e-02;

			    }
				
				else if ((x > 50) && (x <= 75))   /* foredune front slop  */ {
				
				//scalar u_x = ((u_star1) / (k_van_karman1))* (log((y+(z_01)) / (z_01)));
                
				Ks_fun1=(((x-50)/(75-50))*(2.400000e-01-5.000000e-02))+5.000000e-02;
				
			    }
				
				else if ((x > 75) && (x <= 125))   /* top of foredune  */ {
				
				//scalar u_x = ((u_star1) / (k_van_karman1))* (log((y+(z_01)) / (z_01)));
                
				Ks_fun1=2.400000e-01;

			    }
				
				else if ((x > 125) && (x <= 150))   /* foredune back slop   */ {
				
				//scalar u_x = ((u_star1) / (k_van_karman1))* (log((y+(z_01)) / (z_01)));
                
				Ks_fun1=2.400000e-01-(((x-125)/(150-125))*(2.400000e-01-1.900000e-01));

			    }

				else  /* Lee of foredune  */ {
					
					Ks_fun1=1.900000e-01;
					
				}
				
					
				std::ofstream write_x_roughness;
	            write_x_roughness.open("write_x_roughness", std::ofstream::out | std::ofstream::app);  
	            write_x_roughness.precision(20);
	            write_x_roughness << x << "	" << Ks_fun1 << "\n";
	            write_x_roughness.close();
				
				
				/*if (Pstream::master()) 
				/{
					
				std::ofstream write_x_roughness;
	            write_x_roughness.open("write_x_roughness", std::ofstream::out | std::ofstream::app);  
	            write_x_roughness.precision(20);
	            write_x_roughness << x << "	" << Ks_fun1 << "\n";
	            write_x_roughness.close();
				
				}*/
				 
				 Ks_fun[i] = Ks_fun1;
			}
			
			//U.writeEntry("", os);  // Error
			
			writeEntry(os, "", Ks_fun);
//}}} end code
    }
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

// ************************************************************************* //

