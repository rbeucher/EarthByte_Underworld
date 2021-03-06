/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**
** Copyright (C), 2003, Victorian Partnership for Advanced Computing (VPAC) Ltd, 110 Victoria Street, Melbourne, 3053, Australia.
**
** Authors:
**	Stevan M. Quenette, Senior Software Engineer, VPAC. (steve@vpac.org)
**	Patrick D. Sunter, Software Engineer, VPAC. (pds@vpac.org)
**	Luke J. Hodkinson, Computational Engineer, VPAC. (lhodkins@vpac.org)
**	Siew-Ching Tan, Software Engineer, VPAC. (siew@vpac.org)
**	Alan H. Lo, Computational Engineer, VPAC. (alan@vpac.org)
**	Raquibul Hassan, Computational Engineer, VPAC. (raq@vpac.org)
**
**  This library is free software; you can redistribute it and/or
**  modify it under the terms of the GNU Lesser General Public
**  License as published by the Free Software Foundation; either
**  version 2.1 of the License, or (at your option) any later version.
**
**  This library is distributed in the hope that it will be useful,
**  but WITHOUT ANY WARRANTY; without even the implied warranty of
**  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
**  Lesser General Public License for more details.
**
**  You should have received a copy of the GNU Lesser General Public
**  License along with this library; if not, write to the Free Software
**  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
**
*/
/** \file
**  Role:
**
** Assumptions:
**
** Invariants:
**
** Comments:
**
**
**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

#ifndef __StgDomain_Mesh_ProjectionAlgorithms_h__
#define __StgDomain_Mesh_ProjectionAlgorithms_h__

	/** Textual name of this class */
	extern const Type Mesh_ProjectionAlgorithms_Type;

	/** Virtual function types */

	/** Class contents */
	#define __Mesh_ProjectionAlgorithms		\
		/* General info */			\
		__Mesh_Algorithms			\
							\
		/* Virtual info */			\
							\
		/* Mesh_ProjectionAlgorithms info */	\
		double   sres[3];    /* the spherical resolution in (theta, radius phi) */  \
		double   smincrd[3]; /* spherical mesh min coords (theta, radius phi) */ \
		double   smaxcrd[3]; /* spherical mesh max coords (theta, radius phi) */

	struct Mesh_ProjectionAlgorithms { __Mesh_ProjectionAlgorithms };

	/*--------------------------------------------------------------------------------------------------------------------------
	** Constructors
	*/



	Mesh_ProjectionAlgorithms* Mesh_ProjectionAlgorithms_New( Name name, AbstractContext* context );

	
	#ifndef ZERO
	#define ZERO 0
	#endif

	#define MESH_REGULARALGORITHMS_DEFARGS \
                MESH_ALGORITHMS_DEFARGS

	#define MESH_REGULARALGORITHMS_PASSARGS \
                MESH_ALGORITHMS_PASSARGS

	Mesh_ProjectionAlgorithms* _Mesh_ProjectionAlgorithms_New(  MESH_REGULARALGORITHMS_DEFARGS  );

	/*--------------------------------------------------------------------------------------------------------------------------
	** Virtual functions
	*/

	void _Mesh_ProjectionAlgorithms_Init( void* algorithms );

	void _Mesh_ProjectionAlgorithms_Delete( void* algorithms );

	void _Mesh_ProjectionAlgorithms_Print( void* algorithms, Stream* stream );

	void _Mesh_ProjectionAlgorithms_AssignFromXML( void* algorithms, Stg_ComponentFactory* cf, void* data );

	void _Mesh_ProjectionAlgorithms_Build( void* algorithms, void* data );

	void _Mesh_ProjectionAlgorithms_Initialise( void* algorithms, void* data );

	void _Mesh_ProjectionAlgorithms_Execute( void* algorithms, void* data );

	void _Mesh_ProjectionAlgorithms_Destroy( void* algorithms, void* data );


	/*--------------------------------------------------------------------------------------------------------------------------
	** Public functions
	*/

	void Mesh_ProjectionAlgorithms_SetMesh( void* algorithms, void* mesh );

	void Mesh_ProjectionAlgorithms_Update( void* algorithms );

	Bool Mesh_ProjectionAlgorithms_Search( void* algorithms, void* mesh, double* point, MeshTopology_Dim* dim, unsigned* ind );

	Bool Mesh_ProjectionAlgorithms_SearchElements( void* algorithms, double* point, unsigned* elInd );

   Bool Mesh_ProjectionAlgorithms_ElementHasPointGeneral(
      void*             hexType,
      unsigned          elInd,
      double*           point, 
      MeshTopology_Dim* dim,
      unsigned*         ind );

   Bool Mesh_ProjectionAlgorithms_ElementHasPoint(
      void*             hexType,
      unsigned          elInd,
      double*           point, 
      MeshTopology_Dim* dim,
      unsigned*         ind );

	double Mesh_ProjectionAlgorithms_GetMinimumSeparation( void* algorithms, void* mesh, double* perDim );

	void Mesh_ProjectionAlgorithms_GetLocalCoordRange( void* algorithms, void* mesh, double* min, double* max );

	void Mesh_ProjectionAlgorithms_GetDomainCoordRange( void* algorithms, void* mesh, double* min, double* max );

	void Mesh_ProjectionAlgorithms_GetGlobalCoordRange( void* algorithms, void* mesh, double* min, double* max );

	/*--------------------------------------------------------------------------------------------------------------------------
	** Private Member functions
	*/

	void Mesh_ProjectionAlgorithms_Destruct( Mesh_ProjectionAlgorithms* self );

#endif /* __StgDomain_Mesh_ProjectionAlgorithms_h__ */

