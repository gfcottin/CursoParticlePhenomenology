ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_345 = (1.000000D+00*MDL_COMPLEXI*MDL_G2*(MDL_ZUL11
     $ *MDL_CONJG__ZDL11+MDL_ZUL12*MDL_CONJG__ZDL12+MDL_ZUL13
     $ *MDL_CONJG__ZDL13))/MDL_SQRT__2
      GC_346 = (1.000000D+00*MDL_COMPLEXI*MDL_G2*(MDL_ZUL11
     $ *MDL_CONJG__ZDL21+MDL_ZUL12*MDL_CONJG__ZDL22+MDL_ZUL13
     $ *MDL_CONJG__ZDL23))/MDL_SQRT__2
      GC_348 = (1.000000D+00*MDL_COMPLEXI*MDL_G2*(MDL_ZUL21
     $ *MDL_CONJG__ZDL11+MDL_ZUL22*MDL_CONJG__ZDL12+MDL_ZUL23
     $ *MDL_CONJG__ZDL13))/MDL_SQRT__2
      GC_349 = (1.000000D+00*MDL_COMPLEXI*MDL_G2*(MDL_ZUL21
     $ *MDL_CONJG__ZDL21+MDL_ZUL22*MDL_CONJG__ZDL22+MDL_ZUL23
     $ *MDL_CONJG__ZDL23))/MDL_SQRT__2
      GC_462 = (1.000000D+00*MDL_COMPLEXI*MDL_G2*(MDL_ZEL11
     $ *MDL_CONJG__VV41+MDL_ZEL12*MDL_CONJG__VV42+MDL_ZEL13
     $ *MDL_CONJG__VV43))/MDL_SQRT__2
      END
