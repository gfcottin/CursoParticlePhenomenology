from object_library import all_couplings,Coupling 
from cmath import exp 
from function_library import complexconjugate,re,im,csc,sec,acsc,asec 
 
 
GC_1 = Coupling(name = 'GC_1',
	 value = '-1*complex(0,1)*v*complexconjugate(Lam)', 
	 order = {'QED':1} ) 
 
GC_2 = Coupling(name = 'GC_2',
	 value = '-3*complex(0,1)*v*complexconjugate(Lam)', 
	 order = {'QED':1} ) 
 
GC_3 = Coupling(name = 'GC_3',
	 value = '-1*complex(0,1)*v*complexconjugate(Lam)', 
	 order = {'QED':1} ) 
 
GC_4 = Coupling(name = 'GC_4',
	 value = '1./2.*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_5 = Coupling(name = 'GC_5',
	 value = '1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))**2', 
	 order = {'QED':2} ) 
 
GC_6 = Coupling(name = 'GC_6',
	 value = '(g1*g2*cmath.cos(TW))/2.', 
	 order = {'QED':2} ) 
 
GC_7 = Coupling(name = 'GC_7',
	 value = '-(g1*g2*cmath.sin(TW))/2.', 
	 order = {'QED':2} ) 
 
GC_8 = Coupling(name = 'GC_8',
	 value = '-(g1*g2*cmath.cos(TW))/2.', 
	 order = {'QED':2} ) 
 
GC_9 = Coupling(name = 'GC_9',
	 value = '(g1*g2*cmath.sin(TW))/2.', 
	 order = {'QED':2} ) 
 
GC_10 = Coupling(name = 'GC_10',
	 value = '1./2.*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_11 = Coupling(name = 'GC_11',
	 value = '1./2.*complex(0,1)*(g2*cmath.cos(TW) + g1*cmath.sin(TW))**2', 
	 order = {'QED':2} ) 
 
GC_12 = Coupling(name = 'GC_12',
	 value = '1./2.*complex(0,1)*g1*g2*cmath.cos(TW)', 
	 order = {'QED':2} ) 
 
GC_13 = Coupling(name = 'GC_13',
	 value = '-1./2.*complex(0,1)*g1*g2*cmath.sin(TW)', 
	 order = {'QED':2} ) 
 
GC_14 = Coupling(name = 'GC_14',
	 value = '1./2.*complex(0,1)*g1*g2*cmath.cos(TW)', 
	 order = {'QED':2} ) 
 
GC_15 = Coupling(name = 'GC_15',
	 value = '-1./2.*complex(0,1)*g1*g2*cmath.sin(TW)', 
	 order = {'QED':2} ) 
 
GC_16 = Coupling(name = 'GC_16',
	 value = '1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))**2', 
	 order = {'QED':2} ) 
 
GC_17 = Coupling(name = 'GC_17',
	 value = '-1./4.*complex(0,1)*(-2*g1*g2*cmath.cos(2*TW) + (g1**2 - g2**2)*cmath.sin(2*TW))', 
	 order = {'QED':2} ) 
 
GC_18 = Coupling(name = 'GC_18',
	 value = '1./2.*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_19 = Coupling(name = 'GC_19',
	 value = '1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))**2', 
	 order = {'QED':2} ) 
 
GC_20 = Coupling(name = 'GC_20',
	 value = '(g2*cmath.cos(TW) + g1*cmath.sin(TW))/2.', 
	 order = {'QED':1} ) 
 
GC_21 = Coupling(name = 'GC_21',
	 value = '-g2/2.', 
	 order = {'QED':1} ) 
 
GC_22 = Coupling(name = 'GC_22',
	 value = '-g2/2.', 
	 order = {'QED':1} ) 
 
GC_23 = Coupling(name = 'GC_23',
	 value = '-1./2.*complex(0,1)*g2', 
	 order = {'QED':1} ) 
 
GC_24 = Coupling(name = 'GC_24',
	 value = '1./2.*complex(0,1)*g2', 
	 order = {'QED':1} ) 
 
GC_25 = Coupling(name = 'GC_25',
	 value = '1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_26 = Coupling(name = 'GC_26',
	 value = '1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_27 = Coupling(name = 'GC_27',
	 value = '1./2.*complex(0,1)*g2**2*v', 
	 order = {'QED':1} ) 
 
GC_28 = Coupling(name = 'GC_28',
	 value = '1./2.*complex(0,1)*v*(g2*cmath.cos(TW) + g1*cmath.sin(TW))**2', 
	 order = {'QED':1} ) 
 
GC_29 = Coupling(name = 'GC_29',
	 value = '1./2.*complex(0,1)*g1*g2*v*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_30 = Coupling(name = 'GC_30',
	 value = '-1./2.*complex(0,1)*g1*g2*v*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_31 = Coupling(name = 'GC_31',
	 value = '1./2.*complex(0,1)*g1*g2*v*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_32 = Coupling(name = 'GC_32',
	 value = '-1./2.*complex(0,1)*g1*g2*v*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_33 = Coupling(name = 'GC_33',
	 value = '-((complexconjugate(ZDL11)*(Yd11*complexconjugate(ZDR11) + Yd21*complexconjugate(ZDR12) + Yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL12)*(Yd12*complexconjugate(ZDR11) + Yd22*complexconjugate(ZDR12) + Yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL13)*(Yd13*complexconjugate(ZDR11) + Yd23*complexconjugate(ZDR12) + Yd33*complexconjugate(ZDR13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_34 = Coupling(name = 'GC_34',
	 value = '(ZDL11*(ZDR11*complexconjugate(Yd11) + ZDR12*complexconjugate(Yd21) + ZDR13*complexconjugate(Yd31)) + ZDL12*(ZDR11*complexconjugate(Yd12) + ZDR12*complexconjugate(Yd22) + ZDR13*complexconjugate(Yd32)) + ZDL13*(ZDR11*complexconjugate(Yd13) + ZDR12*complexconjugate(Yd23) + ZDR13*complexconjugate(Yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_35 = Coupling(name = 'GC_35',
	 value = '-((complexconjugate(ZDL21)*(Yd11*complexconjugate(ZDR11) + Yd21*complexconjugate(ZDR12) + Yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL22)*(Yd12*complexconjugate(ZDR11) + Yd22*complexconjugate(ZDR12) + Yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL23)*(Yd13*complexconjugate(ZDR11) + Yd23*complexconjugate(ZDR12) + Yd33*complexconjugate(ZDR13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_36 = Coupling(name = 'GC_36',
	 value = '(ZDL11*(ZDR21*complexconjugate(Yd11) + ZDR22*complexconjugate(Yd21) + ZDR23*complexconjugate(Yd31)) + ZDL12*(ZDR21*complexconjugate(Yd12) + ZDR22*complexconjugate(Yd22) + ZDR23*complexconjugate(Yd32)) + ZDL13*(ZDR21*complexconjugate(Yd13) + ZDR22*complexconjugate(Yd23) + ZDR23*complexconjugate(Yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_37 = Coupling(name = 'GC_37',
	 value = '-((complexconjugate(ZDL31)*(Yd11*complexconjugate(ZDR11) + Yd21*complexconjugate(ZDR12) + Yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL32)*(Yd12*complexconjugate(ZDR11) + Yd22*complexconjugate(ZDR12) + Yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL33)*(Yd13*complexconjugate(ZDR11) + Yd23*complexconjugate(ZDR12) + Yd33*complexconjugate(ZDR13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_38 = Coupling(name = 'GC_38',
	 value = '(ZDL11*(ZDR31*complexconjugate(Yd11) + ZDR32*complexconjugate(Yd21) + ZDR33*complexconjugate(Yd31)) + ZDL12*(ZDR31*complexconjugate(Yd12) + ZDR32*complexconjugate(Yd22) + ZDR33*complexconjugate(Yd32)) + ZDL13*(ZDR31*complexconjugate(Yd13) + ZDR32*complexconjugate(Yd23) + ZDR33*complexconjugate(Yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_39 = Coupling(name = 'GC_39',
	 value = '-((complexconjugate(ZDL11)*(Yd11*complexconjugate(ZDR21) + Yd21*complexconjugate(ZDR22) + Yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL12)*(Yd12*complexconjugate(ZDR21) + Yd22*complexconjugate(ZDR22) + Yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL13)*(Yd13*complexconjugate(ZDR21) + Yd23*complexconjugate(ZDR22) + Yd33*complexconjugate(ZDR23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_40 = Coupling(name = 'GC_40',
	 value = '(ZDL21*(ZDR11*complexconjugate(Yd11) + ZDR12*complexconjugate(Yd21) + ZDR13*complexconjugate(Yd31)) + ZDL22*(ZDR11*complexconjugate(Yd12) + ZDR12*complexconjugate(Yd22) + ZDR13*complexconjugate(Yd32)) + ZDL23*(ZDR11*complexconjugate(Yd13) + ZDR12*complexconjugate(Yd23) + ZDR13*complexconjugate(Yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_41 = Coupling(name = 'GC_41',
	 value = '-((complexconjugate(ZDL21)*(Yd11*complexconjugate(ZDR21) + Yd21*complexconjugate(ZDR22) + Yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL22)*(Yd12*complexconjugate(ZDR21) + Yd22*complexconjugate(ZDR22) + Yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL23)*(Yd13*complexconjugate(ZDR21) + Yd23*complexconjugate(ZDR22) + Yd33*complexconjugate(ZDR23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_42 = Coupling(name = 'GC_42',
	 value = '(ZDL21*(ZDR21*complexconjugate(Yd11) + ZDR22*complexconjugate(Yd21) + ZDR23*complexconjugate(Yd31)) + ZDL22*(ZDR21*complexconjugate(Yd12) + ZDR22*complexconjugate(Yd22) + ZDR23*complexconjugate(Yd32)) + ZDL23*(ZDR21*complexconjugate(Yd13) + ZDR22*complexconjugate(Yd23) + ZDR23*complexconjugate(Yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_43 = Coupling(name = 'GC_43',
	 value = '-((complexconjugate(ZDL31)*(Yd11*complexconjugate(ZDR21) + Yd21*complexconjugate(ZDR22) + Yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL32)*(Yd12*complexconjugate(ZDR21) + Yd22*complexconjugate(ZDR22) + Yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL33)*(Yd13*complexconjugate(ZDR21) + Yd23*complexconjugate(ZDR22) + Yd33*complexconjugate(ZDR23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_44 = Coupling(name = 'GC_44',
	 value = '(ZDL21*(ZDR31*complexconjugate(Yd11) + ZDR32*complexconjugate(Yd21) + ZDR33*complexconjugate(Yd31)) + ZDL22*(ZDR31*complexconjugate(Yd12) + ZDR32*complexconjugate(Yd22) + ZDR33*complexconjugate(Yd32)) + ZDL23*(ZDR31*complexconjugate(Yd13) + ZDR32*complexconjugate(Yd23) + ZDR33*complexconjugate(Yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_45 = Coupling(name = 'GC_45',
	 value = '-((complexconjugate(ZDL11)*(Yd11*complexconjugate(ZDR31) + Yd21*complexconjugate(ZDR32) + Yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL12)*(Yd12*complexconjugate(ZDR31) + Yd22*complexconjugate(ZDR32) + Yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL13)*(Yd13*complexconjugate(ZDR31) + Yd23*complexconjugate(ZDR32) + Yd33*complexconjugate(ZDR33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_46 = Coupling(name = 'GC_46',
	 value = '(ZDL31*(ZDR11*complexconjugate(Yd11) + ZDR12*complexconjugate(Yd21) + ZDR13*complexconjugate(Yd31)) + ZDL32*(ZDR11*complexconjugate(Yd12) + ZDR12*complexconjugate(Yd22) + ZDR13*complexconjugate(Yd32)) + ZDL33*(ZDR11*complexconjugate(Yd13) + ZDR12*complexconjugate(Yd23) + ZDR13*complexconjugate(Yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_47 = Coupling(name = 'GC_47',
	 value = '-((complexconjugate(ZDL21)*(Yd11*complexconjugate(ZDR31) + Yd21*complexconjugate(ZDR32) + Yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL22)*(Yd12*complexconjugate(ZDR31) + Yd22*complexconjugate(ZDR32) + Yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL23)*(Yd13*complexconjugate(ZDR31) + Yd23*complexconjugate(ZDR32) + Yd33*complexconjugate(ZDR33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_48 = Coupling(name = 'GC_48',
	 value = '(ZDL31*(ZDR21*complexconjugate(Yd11) + ZDR22*complexconjugate(Yd21) + ZDR23*complexconjugate(Yd31)) + ZDL32*(ZDR21*complexconjugate(Yd12) + ZDR22*complexconjugate(Yd22) + ZDR23*complexconjugate(Yd32)) + ZDL33*(ZDR21*complexconjugate(Yd13) + ZDR22*complexconjugate(Yd23) + ZDR23*complexconjugate(Yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_49 = Coupling(name = 'GC_49',
	 value = '-((complexconjugate(ZDL31)*(Yd11*complexconjugate(ZDR31) + Yd21*complexconjugate(ZDR32) + Yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL32)*(Yd12*complexconjugate(ZDR31) + Yd22*complexconjugate(ZDR32) + Yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL33)*(Yd13*complexconjugate(ZDR31) + Yd23*complexconjugate(ZDR32) + Yd33*complexconjugate(ZDR33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_50 = Coupling(name = 'GC_50',
	 value = '(ZDL31*(ZDR31*complexconjugate(Yd11) + ZDR32*complexconjugate(Yd21) + ZDR33*complexconjugate(Yd31)) + ZDL32*(ZDR31*complexconjugate(Yd12) + ZDR32*complexconjugate(Yd22) + ZDR33*complexconjugate(Yd32)) + ZDL33*(ZDR31*complexconjugate(Yd13) + ZDR32*complexconjugate(Yd23) + ZDR33*complexconjugate(Yd33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_51 = Coupling(name = 'GC_51',
	 value = '-((complexconjugate(ZEL11)*(Ye11*complexconjugate(ZER11) + Ye21*complexconjugate(ZER12) + Ye31*complexconjugate(ZER13)) + complexconjugate(ZEL12)*(Ye12*complexconjugate(ZER11) + Ye22*complexconjugate(ZER12) + Ye32*complexconjugate(ZER13)) + complexconjugate(ZEL13)*(Ye13*complexconjugate(ZER11) + Ye23*complexconjugate(ZER12) + Ye33*complexconjugate(ZER13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_52 = Coupling(name = 'GC_52',
	 value = '(ZEL11*(ZER11*complexconjugate(Ye11) + ZER12*complexconjugate(Ye21) + ZER13*complexconjugate(Ye31)) + ZEL12*(ZER11*complexconjugate(Ye12) + ZER12*complexconjugate(Ye22) + ZER13*complexconjugate(Ye32)) + ZEL13*(ZER11*complexconjugate(Ye13) + ZER12*complexconjugate(Ye23) + ZER13*complexconjugate(Ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_53 = Coupling(name = 'GC_53',
	 value = '-((complexconjugate(ZEL21)*(Ye11*complexconjugate(ZER11) + Ye21*complexconjugate(ZER12) + Ye31*complexconjugate(ZER13)) + complexconjugate(ZEL22)*(Ye12*complexconjugate(ZER11) + Ye22*complexconjugate(ZER12) + Ye32*complexconjugate(ZER13)) + complexconjugate(ZEL23)*(Ye13*complexconjugate(ZER11) + Ye23*complexconjugate(ZER12) + Ye33*complexconjugate(ZER13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_54 = Coupling(name = 'GC_54',
	 value = '(ZEL11*(ZER21*complexconjugate(Ye11) + ZER22*complexconjugate(Ye21) + ZER23*complexconjugate(Ye31)) + ZEL12*(ZER21*complexconjugate(Ye12) + ZER22*complexconjugate(Ye22) + ZER23*complexconjugate(Ye32)) + ZEL13*(ZER21*complexconjugate(Ye13) + ZER22*complexconjugate(Ye23) + ZER23*complexconjugate(Ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_55 = Coupling(name = 'GC_55',
	 value = '-((complexconjugate(ZEL31)*(Ye11*complexconjugate(ZER11) + Ye21*complexconjugate(ZER12) + Ye31*complexconjugate(ZER13)) + complexconjugate(ZEL32)*(Ye12*complexconjugate(ZER11) + Ye22*complexconjugate(ZER12) + Ye32*complexconjugate(ZER13)) + complexconjugate(ZEL33)*(Ye13*complexconjugate(ZER11) + Ye23*complexconjugate(ZER12) + Ye33*complexconjugate(ZER13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_56 = Coupling(name = 'GC_56',
	 value = '(ZEL11*(ZER31*complexconjugate(Ye11) + ZER32*complexconjugate(Ye21) + ZER33*complexconjugate(Ye31)) + ZEL12*(ZER31*complexconjugate(Ye12) + ZER32*complexconjugate(Ye22) + ZER33*complexconjugate(Ye32)) + ZEL13*(ZER31*complexconjugate(Ye13) + ZER32*complexconjugate(Ye23) + ZER33*complexconjugate(Ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_57 = Coupling(name = 'GC_57',
	 value = '-((complexconjugate(ZEL11)*(Ye11*complexconjugate(ZER21) + Ye21*complexconjugate(ZER22) + Ye31*complexconjugate(ZER23)) + complexconjugate(ZEL12)*(Ye12*complexconjugate(ZER21) + Ye22*complexconjugate(ZER22) + Ye32*complexconjugate(ZER23)) + complexconjugate(ZEL13)*(Ye13*complexconjugate(ZER21) + Ye23*complexconjugate(ZER22) + Ye33*complexconjugate(ZER23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_58 = Coupling(name = 'GC_58',
	 value = '(ZEL21*(ZER11*complexconjugate(Ye11) + ZER12*complexconjugate(Ye21) + ZER13*complexconjugate(Ye31)) + ZEL22*(ZER11*complexconjugate(Ye12) + ZER12*complexconjugate(Ye22) + ZER13*complexconjugate(Ye32)) + ZEL23*(ZER11*complexconjugate(Ye13) + ZER12*complexconjugate(Ye23) + ZER13*complexconjugate(Ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_59 = Coupling(name = 'GC_59',
	 value = '-((complexconjugate(ZEL21)*(Ye11*complexconjugate(ZER21) + Ye21*complexconjugate(ZER22) + Ye31*complexconjugate(ZER23)) + complexconjugate(ZEL22)*(Ye12*complexconjugate(ZER21) + Ye22*complexconjugate(ZER22) + Ye32*complexconjugate(ZER23)) + complexconjugate(ZEL23)*(Ye13*complexconjugate(ZER21) + Ye23*complexconjugate(ZER22) + Ye33*complexconjugate(ZER23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_60 = Coupling(name = 'GC_60',
	 value = '(ZEL21*(ZER21*complexconjugate(Ye11) + ZER22*complexconjugate(Ye21) + ZER23*complexconjugate(Ye31)) + ZEL22*(ZER21*complexconjugate(Ye12) + ZER22*complexconjugate(Ye22) + ZER23*complexconjugate(Ye32)) + ZEL23*(ZER21*complexconjugate(Ye13) + ZER22*complexconjugate(Ye23) + ZER23*complexconjugate(Ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_61 = Coupling(name = 'GC_61',
	 value = '-((complexconjugate(ZEL31)*(Ye11*complexconjugate(ZER21) + Ye21*complexconjugate(ZER22) + Ye31*complexconjugate(ZER23)) + complexconjugate(ZEL32)*(Ye12*complexconjugate(ZER21) + Ye22*complexconjugate(ZER22) + Ye32*complexconjugate(ZER23)) + complexconjugate(ZEL33)*(Ye13*complexconjugate(ZER21) + Ye23*complexconjugate(ZER22) + Ye33*complexconjugate(ZER23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_62 = Coupling(name = 'GC_62',
	 value = '(ZEL21*(ZER31*complexconjugate(Ye11) + ZER32*complexconjugate(Ye21) + ZER33*complexconjugate(Ye31)) + ZEL22*(ZER31*complexconjugate(Ye12) + ZER32*complexconjugate(Ye22) + ZER33*complexconjugate(Ye32)) + ZEL23*(ZER31*complexconjugate(Ye13) + ZER32*complexconjugate(Ye23) + ZER33*complexconjugate(Ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_63 = Coupling(name = 'GC_63',
	 value = '-((complexconjugate(ZEL11)*(Ye11*complexconjugate(ZER31) + Ye21*complexconjugate(ZER32) + Ye31*complexconjugate(ZER33)) + complexconjugate(ZEL12)*(Ye12*complexconjugate(ZER31) + Ye22*complexconjugate(ZER32) + Ye32*complexconjugate(ZER33)) + complexconjugate(ZEL13)*(Ye13*complexconjugate(ZER31) + Ye23*complexconjugate(ZER32) + Ye33*complexconjugate(ZER33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_64 = Coupling(name = 'GC_64',
	 value = '(ZEL31*(ZER11*complexconjugate(Ye11) + ZER12*complexconjugate(Ye21) + ZER13*complexconjugate(Ye31)) + ZEL32*(ZER11*complexconjugate(Ye12) + ZER12*complexconjugate(Ye22) + ZER13*complexconjugate(Ye32)) + ZEL33*(ZER11*complexconjugate(Ye13) + ZER12*complexconjugate(Ye23) + ZER13*complexconjugate(Ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_65 = Coupling(name = 'GC_65',
	 value = '-((complexconjugate(ZEL21)*(Ye11*complexconjugate(ZER31) + Ye21*complexconjugate(ZER32) + Ye31*complexconjugate(ZER33)) + complexconjugate(ZEL22)*(Ye12*complexconjugate(ZER31) + Ye22*complexconjugate(ZER32) + Ye32*complexconjugate(ZER33)) + complexconjugate(ZEL23)*(Ye13*complexconjugate(ZER31) + Ye23*complexconjugate(ZER32) + Ye33*complexconjugate(ZER33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_66 = Coupling(name = 'GC_66',
	 value = '(ZEL31*(ZER21*complexconjugate(Ye11) + ZER22*complexconjugate(Ye21) + ZER23*complexconjugate(Ye31)) + ZEL32*(ZER21*complexconjugate(Ye12) + ZER22*complexconjugate(Ye22) + ZER23*complexconjugate(Ye32)) + ZEL33*(ZER21*complexconjugate(Ye13) + ZER22*complexconjugate(Ye23) + ZER23*complexconjugate(Ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_67 = Coupling(name = 'GC_67',
	 value = '-((complexconjugate(ZEL31)*(Ye11*complexconjugate(ZER31) + Ye21*complexconjugate(ZER32) + Ye31*complexconjugate(ZER33)) + complexconjugate(ZEL32)*(Ye12*complexconjugate(ZER31) + Ye22*complexconjugate(ZER32) + Ye32*complexconjugate(ZER33)) + complexconjugate(ZEL33)*(Ye13*complexconjugate(ZER31) + Ye23*complexconjugate(ZER32) + Ye33*complexconjugate(ZER33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_68 = Coupling(name = 'GC_68',
	 value = '(ZEL31*(ZER31*complexconjugate(Ye11) + ZER32*complexconjugate(Ye21) + ZER33*complexconjugate(Ye31)) + ZEL32*(ZER31*complexconjugate(Ye12) + ZER32*complexconjugate(Ye22) + ZER33*complexconjugate(Ye32)) + ZEL33*(ZER31*complexconjugate(Ye13) + ZER32*complexconjugate(Ye23) + ZER33*complexconjugate(Ye33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_69 = Coupling(name = 'GC_69',
	 value = '-((complexconjugate(ZUL11)*(Yu11*complexconjugate(ZUR11) + Yu21*complexconjugate(ZUR12) + Yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL12)*(Yu12*complexconjugate(ZUR11) + Yu22*complexconjugate(ZUR12) + Yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL13)*(Yu13*complexconjugate(ZUR11) + Yu23*complexconjugate(ZUR12) + Yu33*complexconjugate(ZUR13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_70 = Coupling(name = 'GC_70',
	 value = '(ZUL11*(ZUR11*complexconjugate(Yu11) + ZUR12*complexconjugate(Yu21) + ZUR13*complexconjugate(Yu31)) + ZUL12*(ZUR11*complexconjugate(Yu12) + ZUR12*complexconjugate(Yu22) + ZUR13*complexconjugate(Yu32)) + ZUL13*(ZUR11*complexconjugate(Yu13) + ZUR12*complexconjugate(Yu23) + ZUR13*complexconjugate(Yu33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_71 = Coupling(name = 'GC_71',
	 value = '-((complexconjugate(ZUL21)*(Yu11*complexconjugate(ZUR11) + Yu21*complexconjugate(ZUR12) + Yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL22)*(Yu12*complexconjugate(ZUR11) + Yu22*complexconjugate(ZUR12) + Yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL23)*(Yu13*complexconjugate(ZUR11) + Yu23*complexconjugate(ZUR12) + Yu33*complexconjugate(ZUR13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_72 = Coupling(name = 'GC_72',
	 value = '(ZUL11*(ZUR21*complexconjugate(Yu11) + ZUR22*complexconjugate(Yu21) + ZUR23*complexconjugate(Yu31)) + ZUL12*(ZUR21*complexconjugate(Yu12) + ZUR22*complexconjugate(Yu22) + ZUR23*complexconjugate(Yu32)) + ZUL13*(ZUR21*complexconjugate(Yu13) + ZUR22*complexconjugate(Yu23) + ZUR23*complexconjugate(Yu33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_73 = Coupling(name = 'GC_73',
	 value = '-((complexconjugate(ZUL31)*(Yu11*complexconjugate(ZUR11) + Yu21*complexconjugate(ZUR12) + Yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL32)*(Yu12*complexconjugate(ZUR11) + Yu22*complexconjugate(ZUR12) + Yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL33)*(Yu13*complexconjugate(ZUR11) + Yu23*complexconjugate(ZUR12) + Yu33*complexconjugate(ZUR13)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_74 = Coupling(name = 'GC_74',
	 value = '(ZUL11*(ZUR31*complexconjugate(Yu11) + ZUR32*complexconjugate(Yu21) + ZUR33*complexconjugate(Yu31)) + ZUL12*(ZUR31*complexconjugate(Yu12) + ZUR32*complexconjugate(Yu22) + ZUR33*complexconjugate(Yu32)) + ZUL13*(ZUR31*complexconjugate(Yu13) + ZUR32*complexconjugate(Yu23) + ZUR33*complexconjugate(Yu33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_75 = Coupling(name = 'GC_75',
	 value = '-((complexconjugate(ZUL11)*(Yu11*complexconjugate(ZUR21) + Yu21*complexconjugate(ZUR22) + Yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL12)*(Yu12*complexconjugate(ZUR21) + Yu22*complexconjugate(ZUR22) + Yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL13)*(Yu13*complexconjugate(ZUR21) + Yu23*complexconjugate(ZUR22) + Yu33*complexconjugate(ZUR23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_76 = Coupling(name = 'GC_76',
	 value = '(ZUL21*(ZUR11*complexconjugate(Yu11) + ZUR12*complexconjugate(Yu21) + ZUR13*complexconjugate(Yu31)) + ZUL22*(ZUR11*complexconjugate(Yu12) + ZUR12*complexconjugate(Yu22) + ZUR13*complexconjugate(Yu32)) + ZUL23*(ZUR11*complexconjugate(Yu13) + ZUR12*complexconjugate(Yu23) + ZUR13*complexconjugate(Yu33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_77 = Coupling(name = 'GC_77',
	 value = '-((complexconjugate(ZUL21)*(Yu11*complexconjugate(ZUR21) + Yu21*complexconjugate(ZUR22) + Yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL22)*(Yu12*complexconjugate(ZUR21) + Yu22*complexconjugate(ZUR22) + Yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL23)*(Yu13*complexconjugate(ZUR21) + Yu23*complexconjugate(ZUR22) + Yu33*complexconjugate(ZUR23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_78 = Coupling(name = 'GC_78',
	 value = '(ZUL21*(ZUR21*complexconjugate(Yu11) + ZUR22*complexconjugate(Yu21) + ZUR23*complexconjugate(Yu31)) + ZUL22*(ZUR21*complexconjugate(Yu12) + ZUR22*complexconjugate(Yu22) + ZUR23*complexconjugate(Yu32)) + ZUL23*(ZUR21*complexconjugate(Yu13) + ZUR22*complexconjugate(Yu23) + ZUR23*complexconjugate(Yu33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_79 = Coupling(name = 'GC_79',
	 value = '-((complexconjugate(ZUL31)*(Yu11*complexconjugate(ZUR21) + Yu21*complexconjugate(ZUR22) + Yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL32)*(Yu12*complexconjugate(ZUR21) + Yu22*complexconjugate(ZUR22) + Yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL33)*(Yu13*complexconjugate(ZUR21) + Yu23*complexconjugate(ZUR22) + Yu33*complexconjugate(ZUR23)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_80 = Coupling(name = 'GC_80',
	 value = '(ZUL21*(ZUR31*complexconjugate(Yu11) + ZUR32*complexconjugate(Yu21) + ZUR33*complexconjugate(Yu31)) + ZUL22*(ZUR31*complexconjugate(Yu12) + ZUR32*complexconjugate(Yu22) + ZUR33*complexconjugate(Yu32)) + ZUL23*(ZUR31*complexconjugate(Yu13) + ZUR32*complexconjugate(Yu23) + ZUR33*complexconjugate(Yu33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_81 = Coupling(name = 'GC_81',
	 value = '-((complexconjugate(ZUL11)*(Yu11*complexconjugate(ZUR31) + Yu21*complexconjugate(ZUR32) + Yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL12)*(Yu12*complexconjugate(ZUR31) + Yu22*complexconjugate(ZUR32) + Yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL13)*(Yu13*complexconjugate(ZUR31) + Yu23*complexconjugate(ZUR32) + Yu33*complexconjugate(ZUR33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_82 = Coupling(name = 'GC_82',
	 value = '(ZUL31*(ZUR11*complexconjugate(Yu11) + ZUR12*complexconjugate(Yu21) + ZUR13*complexconjugate(Yu31)) + ZUL32*(ZUR11*complexconjugate(Yu12) + ZUR12*complexconjugate(Yu22) + ZUR13*complexconjugate(Yu32)) + ZUL33*(ZUR11*complexconjugate(Yu13) + ZUR12*complexconjugate(Yu23) + ZUR13*complexconjugate(Yu33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_83 = Coupling(name = 'GC_83',
	 value = '-((complexconjugate(ZUL21)*(Yu11*complexconjugate(ZUR31) + Yu21*complexconjugate(ZUR32) + Yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL22)*(Yu12*complexconjugate(ZUR31) + Yu22*complexconjugate(ZUR32) + Yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL23)*(Yu13*complexconjugate(ZUR31) + Yu23*complexconjugate(ZUR32) + Yu33*complexconjugate(ZUR33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_84 = Coupling(name = 'GC_84',
	 value = '(ZUL31*(ZUR21*complexconjugate(Yu11) + ZUR22*complexconjugate(Yu21) + ZUR23*complexconjugate(Yu31)) + ZUL32*(ZUR21*complexconjugate(Yu12) + ZUR22*complexconjugate(Yu22) + ZUR23*complexconjugate(Yu32)) + ZUL33*(ZUR21*complexconjugate(Yu13) + ZUR22*complexconjugate(Yu23) + ZUR23*complexconjugate(Yu33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_85 = Coupling(name = 'GC_85',
	 value = '-((complexconjugate(ZUL31)*(Yu11*complexconjugate(ZUR31) + Yu21*complexconjugate(ZUR32) + Yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL32)*(Yu12*complexconjugate(ZUR31) + Yu22*complexconjugate(ZUR32) + Yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL33)*(Yu13*complexconjugate(ZUR31) + Yu23*complexconjugate(ZUR32) + Yu33*complexconjugate(ZUR33)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_86 = Coupling(name = 'GC_86',
	 value = '(ZUL31*(ZUR31*complexconjugate(Yu11) + ZUR32*complexconjugate(Yu21) + ZUR33*complexconjugate(Yu31)) + ZUL32*(ZUR31*complexconjugate(Yu12) + ZUR32*complexconjugate(Yu22) + ZUR33*complexconjugate(Yu32)) + ZUL33*(ZUR31*complexconjugate(Yu13) + ZUR32*complexconjugate(Yu23) + ZUR33*complexconjugate(Yu33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_87 = Coupling(name = 'GC_87',
	 value = '-((2*complexconjugate(Vv11)*(Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16)) + 2*complexconjugate(Vv12)*(Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16)) + 2*complexconjugate(Vv13)*(Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_88 = Coupling(name = 'GC_88',
	 value = '(2*Vv11*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + 2*Vv12*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + 2*Vv13*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_89 = Coupling(name = 'GC_89',
	 value = '-(((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(Vv21) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(Vv22) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(Vv23) + complexconjugate(Vv11)*(Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26)) + complexconjugate(Vv12)*(Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26)) + complexconjugate(Vv13)*(Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_90 = Coupling(name = 'GC_90',
	 value = '(Vv21*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + Vv11*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + Vv22*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + Vv12*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + Vv23*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)) + Vv13*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_91 = Coupling(name = 'GC_91',
	 value = '-(((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(Vv31) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(Vv32) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(Vv33) + complexconjugate(Vv11)*(Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36)) + complexconjugate(Vv12)*(Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36)) + complexconjugate(Vv13)*(Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_92 = Coupling(name = 'GC_92',
	 value = '(Vv31*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + Vv11*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + Vv32*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + Vv12*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + Vv33*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)) + Vv13*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_93 = Coupling(name = 'GC_93',
	 value = '-(((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(Vv41) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(Vv42) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(Vv43) + complexconjugate(Vv11)*(Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46)) + complexconjugate(Vv12)*(Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46)) + complexconjugate(Vv13)*(Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_94 = Coupling(name = 'GC_94',
	 value = '(Vv41*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + Vv11*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + Vv42*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + Vv12*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + Vv43*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)) + Vv13*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_95 = Coupling(name = 'GC_95',
	 value = '-(((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(Vv51) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(Vv52) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(Vv53) + complexconjugate(Vv11)*(Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56)) + complexconjugate(Vv12)*(Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56)) + complexconjugate(Vv13)*(Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_96 = Coupling(name = 'GC_96',
	 value = '(Vv51*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + Vv11*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + Vv52*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + Vv12*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + Vv53*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)) + Vv13*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_97 = Coupling(name = 'GC_97',
	 value = '-(((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(Vv61) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(Vv62) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(Vv63) + complexconjugate(Vv11)*(Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66)) + complexconjugate(Vv12)*(Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66)) + complexconjugate(Vv13)*(Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_98 = Coupling(name = 'GC_98',
	 value = '(Vv61*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + Vv11*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + Vv62*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + Vv12*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + Vv63*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)) + Vv13*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_99 = Coupling(name = 'GC_99',
	 value = '-((2*complexconjugate(Vv21)*(Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26)) + 2*complexconjugate(Vv22)*(Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26)) + 2*complexconjugate(Vv23)*(Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_100 = Coupling(name = 'GC_100',
	 value = '(2*Vv21*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + 2*Vv22*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + 2*Vv23*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_101 = Coupling(name = 'GC_101',
	 value = '-(((Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26))*complexconjugate(Vv31) + (Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26))*complexconjugate(Vv32) + (Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))*complexconjugate(Vv33) + complexconjugate(Vv21)*(Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36)) + complexconjugate(Vv22)*(Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36)) + complexconjugate(Vv23)*(Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_102 = Coupling(name = 'GC_102',
	 value = '(Vv31*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + Vv21*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + Vv32*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + Vv22*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + Vv33*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)) + Vv23*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_103 = Coupling(name = 'GC_103',
	 value = '-(((Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26))*complexconjugate(Vv41) + (Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26))*complexconjugate(Vv42) + (Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))*complexconjugate(Vv43) + complexconjugate(Vv21)*(Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46)) + complexconjugate(Vv22)*(Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46)) + complexconjugate(Vv23)*(Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_104 = Coupling(name = 'GC_104',
	 value = '(Vv41*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + Vv21*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + Vv42*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + Vv22*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + Vv43*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)) + Vv23*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_105 = Coupling(name = 'GC_105',
	 value = '-(((Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26))*complexconjugate(Vv51) + (Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26))*complexconjugate(Vv52) + (Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))*complexconjugate(Vv53) + complexconjugate(Vv21)*(Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56)) + complexconjugate(Vv22)*(Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56)) + complexconjugate(Vv23)*(Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_106 = Coupling(name = 'GC_106',
	 value = '(Vv51*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + Vv21*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + Vv52*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + Vv22*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + Vv53*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)) + Vv23*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_107 = Coupling(name = 'GC_107',
	 value = '-(((Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26))*complexconjugate(Vv61) + (Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26))*complexconjugate(Vv62) + (Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))*complexconjugate(Vv63) + complexconjugate(Vv21)*(Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66)) + complexconjugate(Vv22)*(Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66)) + complexconjugate(Vv23)*(Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_108 = Coupling(name = 'GC_108',
	 value = '(Vv61*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + Vv21*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + Vv62*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + Vv22*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + Vv63*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)) + Vv23*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_109 = Coupling(name = 'GC_109',
	 value = '-((2*complexconjugate(Vv31)*(Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36)) + 2*complexconjugate(Vv32)*(Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36)) + 2*complexconjugate(Vv33)*(Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_110 = Coupling(name = 'GC_110',
	 value = '(2*Vv31*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + 2*Vv32*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + 2*Vv33*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_111 = Coupling(name = 'GC_111',
	 value = '-(((Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36))*complexconjugate(Vv41) + (Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36))*complexconjugate(Vv42) + (Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36))*complexconjugate(Vv43) + complexconjugate(Vv31)*(Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46)) + complexconjugate(Vv32)*(Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46)) + complexconjugate(Vv33)*(Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_112 = Coupling(name = 'GC_112',
	 value = '(Vv41*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + Vv31*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + Vv42*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + Vv32*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + Vv43*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33)) + Vv33*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_113 = Coupling(name = 'GC_113',
	 value = '-(((Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36))*complexconjugate(Vv51) + (Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36))*complexconjugate(Vv52) + (Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36))*complexconjugate(Vv53) + complexconjugate(Vv31)*(Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56)) + complexconjugate(Vv32)*(Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56)) + complexconjugate(Vv33)*(Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_114 = Coupling(name = 'GC_114',
	 value = '(Vv51*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + Vv31*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + Vv52*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + Vv32*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + Vv53*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33)) + Vv33*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_115 = Coupling(name = 'GC_115',
	 value = '-(((Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36))*complexconjugate(Vv61) + (Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36))*complexconjugate(Vv62) + (Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36))*complexconjugate(Vv63) + complexconjugate(Vv31)*(Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66)) + complexconjugate(Vv32)*(Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66)) + complexconjugate(Vv33)*(Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_116 = Coupling(name = 'GC_116',
	 value = '(Vv61*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + Vv31*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + Vv62*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + Vv32*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + Vv63*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33)) + Vv33*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_117 = Coupling(name = 'GC_117',
	 value = '-((2*complexconjugate(Vv41)*(Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46)) + 2*complexconjugate(Vv42)*(Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46)) + 2*complexconjugate(Vv43)*(Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_118 = Coupling(name = 'GC_118',
	 value = '(2*Vv41*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + 2*Vv42*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + 2*Vv43*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_119 = Coupling(name = 'GC_119',
	 value = '-(((Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46))*complexconjugate(Vv51) + (Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46))*complexconjugate(Vv52) + (Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46))*complexconjugate(Vv53) + complexconjugate(Vv41)*(Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56)) + complexconjugate(Vv42)*(Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56)) + complexconjugate(Vv43)*(Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_120 = Coupling(name = 'GC_120',
	 value = '(Vv51*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + Vv41*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + Vv52*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + Vv42*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + Vv53*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33)) + Vv43*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_121 = Coupling(name = 'GC_121',
	 value = '-(((Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46))*complexconjugate(Vv61) + (Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46))*complexconjugate(Vv62) + (Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46))*complexconjugate(Vv63) + complexconjugate(Vv41)*(Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66)) + complexconjugate(Vv42)*(Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66)) + complexconjugate(Vv43)*(Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_122 = Coupling(name = 'GC_122',
	 value = '(Vv61*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + Vv41*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + Vv62*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + Vv42*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + Vv63*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33)) + Vv43*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_123 = Coupling(name = 'GC_123',
	 value = '-((2*complexconjugate(Vv51)*(Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56)) + 2*complexconjugate(Vv52)*(Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56)) + 2*complexconjugate(Vv53)*(Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_124 = Coupling(name = 'GC_124',
	 value = '(2*Vv51*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + 2*Vv52*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + 2*Vv53*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_125 = Coupling(name = 'GC_125',
	 value = '-(((Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56))*complexconjugate(Vv61) + (Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56))*complexconjugate(Vv62) + (Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56))*complexconjugate(Vv63) + complexconjugate(Vv51)*(Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66)) + complexconjugate(Vv52)*(Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66)) + complexconjugate(Vv53)*(Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_126 = Coupling(name = 'GC_126',
	 value = '(Vv61*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + Vv51*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + Vv62*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + Vv52*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + Vv63*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33)) + Vv53*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_127 = Coupling(name = 'GC_127',
	 value = '-((2*complexconjugate(Vv61)*(Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66)) + 2*complexconjugate(Vv62)*(Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66)) + 2*complexconjugate(Vv63)*(Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66)))/cmath.sqrt(2))', 
	 order = {'QED':1} ) 
 
GC_128 = Coupling(name = 'GC_128',
	 value = '(2*Vv61*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + 2*Vv62*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + 2*Vv63*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_129 = Coupling(name = 'GC_129',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL11)*(Yd11*complexconjugate(ZDR11) + Yd21*complexconjugate(ZDR12) + Yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL12)*(Yd12*complexconjugate(ZDR11) + Yd22*complexconjugate(ZDR12) + Yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL13)*(Yd13*complexconjugate(ZDR11) + Yd23*complexconjugate(ZDR12) + Yd33*complexconjugate(ZDR13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_130 = Coupling(name = 'GC_130',
	 value = '(-1*complex(0,1)*(ZDL11*(ZDR11*complexconjugate(Yd11) + ZDR12*complexconjugate(Yd21) + ZDR13*complexconjugate(Yd31)) + ZDL12*(ZDR11*complexconjugate(Yd12) + ZDR12*complexconjugate(Yd22) + ZDR13*complexconjugate(Yd32)) + ZDL13*(ZDR11*complexconjugate(Yd13) + ZDR12*complexconjugate(Yd23) + ZDR13*complexconjugate(Yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_131 = Coupling(name = 'GC_131',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL21)*(Yd11*complexconjugate(ZDR11) + Yd21*complexconjugate(ZDR12) + Yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL22)*(Yd12*complexconjugate(ZDR11) + Yd22*complexconjugate(ZDR12) + Yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL23)*(Yd13*complexconjugate(ZDR11) + Yd23*complexconjugate(ZDR12) + Yd33*complexconjugate(ZDR13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_132 = Coupling(name = 'GC_132',
	 value = '(-1*complex(0,1)*(ZDL11*(ZDR21*complexconjugate(Yd11) + ZDR22*complexconjugate(Yd21) + ZDR23*complexconjugate(Yd31)) + ZDL12*(ZDR21*complexconjugate(Yd12) + ZDR22*complexconjugate(Yd22) + ZDR23*complexconjugate(Yd32)) + ZDL13*(ZDR21*complexconjugate(Yd13) + ZDR22*complexconjugate(Yd23) + ZDR23*complexconjugate(Yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_133 = Coupling(name = 'GC_133',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL31)*(Yd11*complexconjugate(ZDR11) + Yd21*complexconjugate(ZDR12) + Yd31*complexconjugate(ZDR13)) + complexconjugate(ZDL32)*(Yd12*complexconjugate(ZDR11) + Yd22*complexconjugate(ZDR12) + Yd32*complexconjugate(ZDR13)) + complexconjugate(ZDL33)*(Yd13*complexconjugate(ZDR11) + Yd23*complexconjugate(ZDR12) + Yd33*complexconjugate(ZDR13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_134 = Coupling(name = 'GC_134',
	 value = '(-1*complex(0,1)*(ZDL11*(ZDR31*complexconjugate(Yd11) + ZDR32*complexconjugate(Yd21) + ZDR33*complexconjugate(Yd31)) + ZDL12*(ZDR31*complexconjugate(Yd12) + ZDR32*complexconjugate(Yd22) + ZDR33*complexconjugate(Yd32)) + ZDL13*(ZDR31*complexconjugate(Yd13) + ZDR32*complexconjugate(Yd23) + ZDR33*complexconjugate(Yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_135 = Coupling(name = 'GC_135',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL11)*(Yd11*complexconjugate(ZDR21) + Yd21*complexconjugate(ZDR22) + Yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL12)*(Yd12*complexconjugate(ZDR21) + Yd22*complexconjugate(ZDR22) + Yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL13)*(Yd13*complexconjugate(ZDR21) + Yd23*complexconjugate(ZDR22) + Yd33*complexconjugate(ZDR23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_136 = Coupling(name = 'GC_136',
	 value = '(-1*complex(0,1)*(ZDL21*(ZDR11*complexconjugate(Yd11) + ZDR12*complexconjugate(Yd21) + ZDR13*complexconjugate(Yd31)) + ZDL22*(ZDR11*complexconjugate(Yd12) + ZDR12*complexconjugate(Yd22) + ZDR13*complexconjugate(Yd32)) + ZDL23*(ZDR11*complexconjugate(Yd13) + ZDR12*complexconjugate(Yd23) + ZDR13*complexconjugate(Yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_137 = Coupling(name = 'GC_137',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL21)*(Yd11*complexconjugate(ZDR21) + Yd21*complexconjugate(ZDR22) + Yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL22)*(Yd12*complexconjugate(ZDR21) + Yd22*complexconjugate(ZDR22) + Yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL23)*(Yd13*complexconjugate(ZDR21) + Yd23*complexconjugate(ZDR22) + Yd33*complexconjugate(ZDR23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_138 = Coupling(name = 'GC_138',
	 value = '(-1*complex(0,1)*(ZDL21*(ZDR21*complexconjugate(Yd11) + ZDR22*complexconjugate(Yd21) + ZDR23*complexconjugate(Yd31)) + ZDL22*(ZDR21*complexconjugate(Yd12) + ZDR22*complexconjugate(Yd22) + ZDR23*complexconjugate(Yd32)) + ZDL23*(ZDR21*complexconjugate(Yd13) + ZDR22*complexconjugate(Yd23) + ZDR23*complexconjugate(Yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_139 = Coupling(name = 'GC_139',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL31)*(Yd11*complexconjugate(ZDR21) + Yd21*complexconjugate(ZDR22) + Yd31*complexconjugate(ZDR23)) + complexconjugate(ZDL32)*(Yd12*complexconjugate(ZDR21) + Yd22*complexconjugate(ZDR22) + Yd32*complexconjugate(ZDR23)) + complexconjugate(ZDL33)*(Yd13*complexconjugate(ZDR21) + Yd23*complexconjugate(ZDR22) + Yd33*complexconjugate(ZDR23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_140 = Coupling(name = 'GC_140',
	 value = '(-1*complex(0,1)*(ZDL21*(ZDR31*complexconjugate(Yd11) + ZDR32*complexconjugate(Yd21) + ZDR33*complexconjugate(Yd31)) + ZDL22*(ZDR31*complexconjugate(Yd12) + ZDR32*complexconjugate(Yd22) + ZDR33*complexconjugate(Yd32)) + ZDL23*(ZDR31*complexconjugate(Yd13) + ZDR32*complexconjugate(Yd23) + ZDR33*complexconjugate(Yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_141 = Coupling(name = 'GC_141',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL11)*(Yd11*complexconjugate(ZDR31) + Yd21*complexconjugate(ZDR32) + Yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL12)*(Yd12*complexconjugate(ZDR31) + Yd22*complexconjugate(ZDR32) + Yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL13)*(Yd13*complexconjugate(ZDR31) + Yd23*complexconjugate(ZDR32) + Yd33*complexconjugate(ZDR33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_142 = Coupling(name = 'GC_142',
	 value = '(-1*complex(0,1)*(ZDL31*(ZDR11*complexconjugate(Yd11) + ZDR12*complexconjugate(Yd21) + ZDR13*complexconjugate(Yd31)) + ZDL32*(ZDR11*complexconjugate(Yd12) + ZDR12*complexconjugate(Yd22) + ZDR13*complexconjugate(Yd32)) + ZDL33*(ZDR11*complexconjugate(Yd13) + ZDR12*complexconjugate(Yd23) + ZDR13*complexconjugate(Yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_143 = Coupling(name = 'GC_143',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL21)*(Yd11*complexconjugate(ZDR31) + Yd21*complexconjugate(ZDR32) + Yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL22)*(Yd12*complexconjugate(ZDR31) + Yd22*complexconjugate(ZDR32) + Yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL23)*(Yd13*complexconjugate(ZDR31) + Yd23*complexconjugate(ZDR32) + Yd33*complexconjugate(ZDR33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_144 = Coupling(name = 'GC_144',
	 value = '(-1*complex(0,1)*(ZDL31*(ZDR21*complexconjugate(Yd11) + ZDR22*complexconjugate(Yd21) + ZDR23*complexconjugate(Yd31)) + ZDL32*(ZDR21*complexconjugate(Yd12) + ZDR22*complexconjugate(Yd22) + ZDR23*complexconjugate(Yd32)) + ZDL33*(ZDR21*complexconjugate(Yd13) + ZDR22*complexconjugate(Yd23) + ZDR23*complexconjugate(Yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_145 = Coupling(name = 'GC_145',
	 value = '(-1*complex(0,1)*(complexconjugate(ZDL31)*(Yd11*complexconjugate(ZDR31) + Yd21*complexconjugate(ZDR32) + Yd31*complexconjugate(ZDR33)) + complexconjugate(ZDL32)*(Yd12*complexconjugate(ZDR31) + Yd22*complexconjugate(ZDR32) + Yd32*complexconjugate(ZDR33)) + complexconjugate(ZDL33)*(Yd13*complexconjugate(ZDR31) + Yd23*complexconjugate(ZDR32) + Yd33*complexconjugate(ZDR33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_146 = Coupling(name = 'GC_146',
	 value = '(-1*complex(0,1)*(ZDL31*(ZDR31*complexconjugate(Yd11) + ZDR32*complexconjugate(Yd21) + ZDR33*complexconjugate(Yd31)) + ZDL32*(ZDR31*complexconjugate(Yd12) + ZDR32*complexconjugate(Yd22) + ZDR33*complexconjugate(Yd32)) + ZDL33*(ZDR31*complexconjugate(Yd13) + ZDR32*complexconjugate(Yd23) + ZDR33*complexconjugate(Yd33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_147 = Coupling(name = 'GC_147',
	 value = '-1*complex(0,1)*(complexconjugate(ZDL11)*(Yu11*complexconjugate(ZUR11) + Yu21*complexconjugate(ZUR12) + Yu31*complexconjugate(ZUR13)) + complexconjugate(ZDL12)*(Yu12*complexconjugate(ZUR11) + Yu22*complexconjugate(ZUR12) + Yu32*complexconjugate(ZUR13)) + complexconjugate(ZDL13)*(Yu13*complexconjugate(ZUR11) + Yu23*complexconjugate(ZUR12) + Yu33*complexconjugate(ZUR13)))', 
	 order = {'QED':1} ) 
 
GC_148 = Coupling(name = 'GC_148',
	 value = '-1*complex(0,1)*(ZUL11*(ZDR11*complexconjugate(Yd11) + ZDR12*complexconjugate(Yd21) + ZDR13*complexconjugate(Yd31)) + ZUL12*(ZDR11*complexconjugate(Yd12) + ZDR12*complexconjugate(Yd22) + ZDR13*complexconjugate(Yd32)) + ZUL13*(ZDR11*complexconjugate(Yd13) + ZDR12*complexconjugate(Yd23) + ZDR13*complexconjugate(Yd33)))', 
	 order = {'QED':1} ) 
 
GC_149 = Coupling(name = 'GC_149',
	 value = '-1*complex(0,1)*(complexconjugate(ZDL21)*(Yu11*complexconjugate(ZUR11) + Yu21*complexconjugate(ZUR12) + Yu31*complexconjugate(ZUR13)) + complexconjugate(ZDL22)*(Yu12*complexconjugate(ZUR11) + Yu22*complexconjugate(ZUR12) + Yu32*complexconjugate(ZUR13)) + complexconjugate(ZDL23)*(Yu13*complexconjugate(ZUR11) + Yu23*complexconjugate(ZUR12) + Yu33*complexconjugate(ZUR13)))', 
	 order = {'QED':1} ) 
 
GC_150 = Coupling(name = 'GC_150',
	 value = '-1*complex(0,1)*(ZUL11*(ZDR21*complexconjugate(Yd11) + ZDR22*complexconjugate(Yd21) + ZDR23*complexconjugate(Yd31)) + ZUL12*(ZDR21*complexconjugate(Yd12) + ZDR22*complexconjugate(Yd22) + ZDR23*complexconjugate(Yd32)) + ZUL13*(ZDR21*complexconjugate(Yd13) + ZDR22*complexconjugate(Yd23) + ZDR23*complexconjugate(Yd33)))', 
	 order = {'QED':1} ) 
 
GC_151 = Coupling(name = 'GC_151',
	 value = '-1*complex(0,1)*(complexconjugate(ZDL31)*(Yu11*complexconjugate(ZUR11) + Yu21*complexconjugate(ZUR12) + Yu31*complexconjugate(ZUR13)) + complexconjugate(ZDL32)*(Yu12*complexconjugate(ZUR11) + Yu22*complexconjugate(ZUR12) + Yu32*complexconjugate(ZUR13)) + complexconjugate(ZDL33)*(Yu13*complexconjugate(ZUR11) + Yu23*complexconjugate(ZUR12) + Yu33*complexconjugate(ZUR13)))', 
	 order = {'QED':1} ) 
 
GC_152 = Coupling(name = 'GC_152',
	 value = '-1*complex(0,1)*(ZUL11*(ZDR31*complexconjugate(Yd11) + ZDR32*complexconjugate(Yd21) + ZDR33*complexconjugate(Yd31)) + ZUL12*(ZDR31*complexconjugate(Yd12) + ZDR32*complexconjugate(Yd22) + ZDR33*complexconjugate(Yd32)) + ZUL13*(ZDR31*complexconjugate(Yd13) + ZDR32*complexconjugate(Yd23) + ZDR33*complexconjugate(Yd33)))', 
	 order = {'QED':1} ) 
 
GC_153 = Coupling(name = 'GC_153',
	 value = '-1*complex(0,1)*(complexconjugate(ZDL11)*(Yu11*complexconjugate(ZUR21) + Yu21*complexconjugate(ZUR22) + Yu31*complexconjugate(ZUR23)) + complexconjugate(ZDL12)*(Yu12*complexconjugate(ZUR21) + Yu22*complexconjugate(ZUR22) + Yu32*complexconjugate(ZUR23)) + complexconjugate(ZDL13)*(Yu13*complexconjugate(ZUR21) + Yu23*complexconjugate(ZUR22) + Yu33*complexconjugate(ZUR23)))', 
	 order = {'QED':1} ) 
 
GC_154 = Coupling(name = 'GC_154',
	 value = '-1*complex(0,1)*(ZUL21*(ZDR11*complexconjugate(Yd11) + ZDR12*complexconjugate(Yd21) + ZDR13*complexconjugate(Yd31)) + ZUL22*(ZDR11*complexconjugate(Yd12) + ZDR12*complexconjugate(Yd22) + ZDR13*complexconjugate(Yd32)) + ZUL23*(ZDR11*complexconjugate(Yd13) + ZDR12*complexconjugate(Yd23) + ZDR13*complexconjugate(Yd33)))', 
	 order = {'QED':1} ) 
 
GC_155 = Coupling(name = 'GC_155',
	 value = '-1*complex(0,1)*(complexconjugate(ZDL21)*(Yu11*complexconjugate(ZUR21) + Yu21*complexconjugate(ZUR22) + Yu31*complexconjugate(ZUR23)) + complexconjugate(ZDL22)*(Yu12*complexconjugate(ZUR21) + Yu22*complexconjugate(ZUR22) + Yu32*complexconjugate(ZUR23)) + complexconjugate(ZDL23)*(Yu13*complexconjugate(ZUR21) + Yu23*complexconjugate(ZUR22) + Yu33*complexconjugate(ZUR23)))', 
	 order = {'QED':1} ) 
 
GC_156 = Coupling(name = 'GC_156',
	 value = '-1*complex(0,1)*(ZUL21*(ZDR21*complexconjugate(Yd11) + ZDR22*complexconjugate(Yd21) + ZDR23*complexconjugate(Yd31)) + ZUL22*(ZDR21*complexconjugate(Yd12) + ZDR22*complexconjugate(Yd22) + ZDR23*complexconjugate(Yd32)) + ZUL23*(ZDR21*complexconjugate(Yd13) + ZDR22*complexconjugate(Yd23) + ZDR23*complexconjugate(Yd33)))', 
	 order = {'QED':1} ) 
 
GC_157 = Coupling(name = 'GC_157',
	 value = '-1*complex(0,1)*(complexconjugate(ZDL31)*(Yu11*complexconjugate(ZUR21) + Yu21*complexconjugate(ZUR22) + Yu31*complexconjugate(ZUR23)) + complexconjugate(ZDL32)*(Yu12*complexconjugate(ZUR21) + Yu22*complexconjugate(ZUR22) + Yu32*complexconjugate(ZUR23)) + complexconjugate(ZDL33)*(Yu13*complexconjugate(ZUR21) + Yu23*complexconjugate(ZUR22) + Yu33*complexconjugate(ZUR23)))', 
	 order = {'QED':1} ) 
 
GC_158 = Coupling(name = 'GC_158',
	 value = '-1*complex(0,1)*(ZUL21*(ZDR31*complexconjugate(Yd11) + ZDR32*complexconjugate(Yd21) + ZDR33*complexconjugate(Yd31)) + ZUL22*(ZDR31*complexconjugate(Yd12) + ZDR32*complexconjugate(Yd22) + ZDR33*complexconjugate(Yd32)) + ZUL23*(ZDR31*complexconjugate(Yd13) + ZDR32*complexconjugate(Yd23) + ZDR33*complexconjugate(Yd33)))', 
	 order = {'QED':1} ) 
 
GC_159 = Coupling(name = 'GC_159',
	 value = '-1*complex(0,1)*(complexconjugate(ZDL11)*(Yu11*complexconjugate(ZUR31) + Yu21*complexconjugate(ZUR32) + Yu31*complexconjugate(ZUR33)) + complexconjugate(ZDL12)*(Yu12*complexconjugate(ZUR31) + Yu22*complexconjugate(ZUR32) + Yu32*complexconjugate(ZUR33)) + complexconjugate(ZDL13)*(Yu13*complexconjugate(ZUR31) + Yu23*complexconjugate(ZUR32) + Yu33*complexconjugate(ZUR33)))', 
	 order = {'QED':1} ) 
 
GC_160 = Coupling(name = 'GC_160',
	 value = '-1*complex(0,1)*(ZUL31*(ZDR11*complexconjugate(Yd11) + ZDR12*complexconjugate(Yd21) + ZDR13*complexconjugate(Yd31)) + ZUL32*(ZDR11*complexconjugate(Yd12) + ZDR12*complexconjugate(Yd22) + ZDR13*complexconjugate(Yd32)) + ZUL33*(ZDR11*complexconjugate(Yd13) + ZDR12*complexconjugate(Yd23) + ZDR13*complexconjugate(Yd33)))', 
	 order = {'QED':1} ) 
 
GC_161 = Coupling(name = 'GC_161',
	 value = '-1*complex(0,1)*(complexconjugate(ZDL21)*(Yu11*complexconjugate(ZUR31) + Yu21*complexconjugate(ZUR32) + Yu31*complexconjugate(ZUR33)) + complexconjugate(ZDL22)*(Yu12*complexconjugate(ZUR31) + Yu22*complexconjugate(ZUR32) + Yu32*complexconjugate(ZUR33)) + complexconjugate(ZDL23)*(Yu13*complexconjugate(ZUR31) + Yu23*complexconjugate(ZUR32) + Yu33*complexconjugate(ZUR33)))', 
	 order = {'QED':1} ) 
 
GC_162 = Coupling(name = 'GC_162',
	 value = '-1*complex(0,1)*(ZUL31*(ZDR21*complexconjugate(Yd11) + ZDR22*complexconjugate(Yd21) + ZDR23*complexconjugate(Yd31)) + ZUL32*(ZDR21*complexconjugate(Yd12) + ZDR22*complexconjugate(Yd22) + ZDR23*complexconjugate(Yd32)) + ZUL33*(ZDR21*complexconjugate(Yd13) + ZDR22*complexconjugate(Yd23) + ZDR23*complexconjugate(Yd33)))', 
	 order = {'QED':1} ) 
 
GC_163 = Coupling(name = 'GC_163',
	 value = '-1*complex(0,1)*(complexconjugate(ZDL31)*(Yu11*complexconjugate(ZUR31) + Yu21*complexconjugate(ZUR32) + Yu31*complexconjugate(ZUR33)) + complexconjugate(ZDL32)*(Yu12*complexconjugate(ZUR31) + Yu22*complexconjugate(ZUR32) + Yu32*complexconjugate(ZUR33)) + complexconjugate(ZDL33)*(Yu13*complexconjugate(ZUR31) + Yu23*complexconjugate(ZUR32) + Yu33*complexconjugate(ZUR33)))', 
	 order = {'QED':1} ) 
 
GC_164 = Coupling(name = 'GC_164',
	 value = '-1*complex(0,1)*(ZUL31*(ZDR31*complexconjugate(Yd11) + ZDR32*complexconjugate(Yd21) + ZDR33*complexconjugate(Yd31)) + ZUL32*(ZDR31*complexconjugate(Yd12) + ZDR32*complexconjugate(Yd22) + ZDR33*complexconjugate(Yd32)) + ZUL33*(ZDR31*complexconjugate(Yd13) + ZDR32*complexconjugate(Yd23) + ZDR33*complexconjugate(Yd33)))', 
	 order = {'QED':1} ) 
 
GC_165 = Coupling(name = 'GC_165',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(ZEL11) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(ZEL12) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_166 = Coupling(name = 'GC_166',
	 value = '-1*complex(0,1)*(Vv11*(ZER11*complexconjugate(Ye11) + ZER12*complexconjugate(Ye21) + ZER13*complexconjugate(Ye31)) + Vv12*(ZER11*complexconjugate(Ye12) + ZER12*complexconjugate(Ye22) + ZER13*complexconjugate(Ye32)) + Vv13*(ZER11*complexconjugate(Ye13) + ZER12*complexconjugate(Ye23) + ZER13*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_167 = Coupling(name = 'GC_167',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(ZEL21) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(ZEL22) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_168 = Coupling(name = 'GC_168',
	 value = '-1*complex(0,1)*(Vv11*(ZER21*complexconjugate(Ye11) + ZER22*complexconjugate(Ye21) + ZER23*complexconjugate(Ye31)) + Vv12*(ZER21*complexconjugate(Ye12) + ZER22*complexconjugate(Ye22) + ZER23*complexconjugate(Ye32)) + Vv13*(ZER21*complexconjugate(Ye13) + ZER22*complexconjugate(Ye23) + ZER23*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_169 = Coupling(name = 'GC_169',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(ZEL31) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(ZEL32) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_170 = Coupling(name = 'GC_170',
	 value = '-1*complex(0,1)*(Vv11*(ZER31*complexconjugate(Ye11) + ZER32*complexconjugate(Ye21) + ZER33*complexconjugate(Ye31)) + Vv12*(ZER31*complexconjugate(Ye12) + ZER32*complexconjugate(Ye22) + ZER33*complexconjugate(Ye32)) + Vv13*(ZER31*complexconjugate(Ye13) + ZER32*complexconjugate(Ye23) + ZER33*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_171 = Coupling(name = 'GC_171',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26))*complexconjugate(ZEL11) + (Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26))*complexconjugate(ZEL12) + (Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_172 = Coupling(name = 'GC_172',
	 value = '-1*complex(0,1)*(Vv21*(ZER11*complexconjugate(Ye11) + ZER12*complexconjugate(Ye21) + ZER13*complexconjugate(Ye31)) + Vv22*(ZER11*complexconjugate(Ye12) + ZER12*complexconjugate(Ye22) + ZER13*complexconjugate(Ye32)) + Vv23*(ZER11*complexconjugate(Ye13) + ZER12*complexconjugate(Ye23) + ZER13*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_173 = Coupling(name = 'GC_173',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26))*complexconjugate(ZEL21) + (Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26))*complexconjugate(ZEL22) + (Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_174 = Coupling(name = 'GC_174',
	 value = '-1*complex(0,1)*(Vv21*(ZER21*complexconjugate(Ye11) + ZER22*complexconjugate(Ye21) + ZER23*complexconjugate(Ye31)) + Vv22*(ZER21*complexconjugate(Ye12) + ZER22*complexconjugate(Ye22) + ZER23*complexconjugate(Ye32)) + Vv23*(ZER21*complexconjugate(Ye13) + ZER22*complexconjugate(Ye23) + ZER23*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_175 = Coupling(name = 'GC_175',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26))*complexconjugate(ZEL31) + (Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26))*complexconjugate(ZEL32) + (Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_176 = Coupling(name = 'GC_176',
	 value = '-1*complex(0,1)*(Vv21*(ZER31*complexconjugate(Ye11) + ZER32*complexconjugate(Ye21) + ZER33*complexconjugate(Ye31)) + Vv22*(ZER31*complexconjugate(Ye12) + ZER32*complexconjugate(Ye22) + ZER33*complexconjugate(Ye32)) + Vv23*(ZER31*complexconjugate(Ye13) + ZER32*complexconjugate(Ye23) + ZER33*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_177 = Coupling(name = 'GC_177',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36))*complexconjugate(ZEL11) + (Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36))*complexconjugate(ZEL12) + (Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36))*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_178 = Coupling(name = 'GC_178',
	 value = '-1*complex(0,1)*(Vv31*(ZER11*complexconjugate(Ye11) + ZER12*complexconjugate(Ye21) + ZER13*complexconjugate(Ye31)) + Vv32*(ZER11*complexconjugate(Ye12) + ZER12*complexconjugate(Ye22) + ZER13*complexconjugate(Ye32)) + Vv33*(ZER11*complexconjugate(Ye13) + ZER12*complexconjugate(Ye23) + ZER13*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_179 = Coupling(name = 'GC_179',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36))*complexconjugate(ZEL21) + (Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36))*complexconjugate(ZEL22) + (Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36))*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_180 = Coupling(name = 'GC_180',
	 value = '-1*complex(0,1)*(Vv31*(ZER21*complexconjugate(Ye11) + ZER22*complexconjugate(Ye21) + ZER23*complexconjugate(Ye31)) + Vv32*(ZER21*complexconjugate(Ye12) + ZER22*complexconjugate(Ye22) + ZER23*complexconjugate(Ye32)) + Vv33*(ZER21*complexconjugate(Ye13) + ZER22*complexconjugate(Ye23) + ZER23*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_181 = Coupling(name = 'GC_181',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36))*complexconjugate(ZEL31) + (Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36))*complexconjugate(ZEL32) + (Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36))*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_182 = Coupling(name = 'GC_182',
	 value = '-1*complex(0,1)*(Vv31*(ZER31*complexconjugate(Ye11) + ZER32*complexconjugate(Ye21) + ZER33*complexconjugate(Ye31)) + Vv32*(ZER31*complexconjugate(Ye12) + ZER32*complexconjugate(Ye22) + ZER33*complexconjugate(Ye32)) + Vv33*(ZER31*complexconjugate(Ye13) + ZER32*complexconjugate(Ye23) + ZER33*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_183 = Coupling(name = 'GC_183',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46))*complexconjugate(ZEL11) + (Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46))*complexconjugate(ZEL12) + (Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46))*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_184 = Coupling(name = 'GC_184',
	 value = '-1*complex(0,1)*(Vv41*(ZER11*complexconjugate(Ye11) + ZER12*complexconjugate(Ye21) + ZER13*complexconjugate(Ye31)) + Vv42*(ZER11*complexconjugate(Ye12) + ZER12*complexconjugate(Ye22) + ZER13*complexconjugate(Ye32)) + Vv43*(ZER11*complexconjugate(Ye13) + ZER12*complexconjugate(Ye23) + ZER13*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_185 = Coupling(name = 'GC_185',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46))*complexconjugate(ZEL21) + (Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46))*complexconjugate(ZEL22) + (Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46))*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_186 = Coupling(name = 'GC_186',
	 value = '-1*complex(0,1)*(Vv41*(ZER21*complexconjugate(Ye11) + ZER22*complexconjugate(Ye21) + ZER23*complexconjugate(Ye31)) + Vv42*(ZER21*complexconjugate(Ye12) + ZER22*complexconjugate(Ye22) + ZER23*complexconjugate(Ye32)) + Vv43*(ZER21*complexconjugate(Ye13) + ZER22*complexconjugate(Ye23) + ZER23*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_187 = Coupling(name = 'GC_187',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46))*complexconjugate(ZEL31) + (Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46))*complexconjugate(ZEL32) + (Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46))*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_188 = Coupling(name = 'GC_188',
	 value = '-1*complex(0,1)*(Vv41*(ZER31*complexconjugate(Ye11) + ZER32*complexconjugate(Ye21) + ZER33*complexconjugate(Ye31)) + Vv42*(ZER31*complexconjugate(Ye12) + ZER32*complexconjugate(Ye22) + ZER33*complexconjugate(Ye32)) + Vv43*(ZER31*complexconjugate(Ye13) + ZER32*complexconjugate(Ye23) + ZER33*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_189 = Coupling(name = 'GC_189',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56))*complexconjugate(ZEL11) + (Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56))*complexconjugate(ZEL12) + (Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56))*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_190 = Coupling(name = 'GC_190',
	 value = '-1*complex(0,1)*(Vv51*(ZER11*complexconjugate(Ye11) + ZER12*complexconjugate(Ye21) + ZER13*complexconjugate(Ye31)) + Vv52*(ZER11*complexconjugate(Ye12) + ZER12*complexconjugate(Ye22) + ZER13*complexconjugate(Ye32)) + Vv53*(ZER11*complexconjugate(Ye13) + ZER12*complexconjugate(Ye23) + ZER13*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_191 = Coupling(name = 'GC_191',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56))*complexconjugate(ZEL21) + (Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56))*complexconjugate(ZEL22) + (Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56))*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_192 = Coupling(name = 'GC_192',
	 value = '-1*complex(0,1)*(Vv51*(ZER21*complexconjugate(Ye11) + ZER22*complexconjugate(Ye21) + ZER23*complexconjugate(Ye31)) + Vv52*(ZER21*complexconjugate(Ye12) + ZER22*complexconjugate(Ye22) + ZER23*complexconjugate(Ye32)) + Vv53*(ZER21*complexconjugate(Ye13) + ZER22*complexconjugate(Ye23) + ZER23*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_193 = Coupling(name = 'GC_193',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56))*complexconjugate(ZEL31) + (Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56))*complexconjugate(ZEL32) + (Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56))*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_194 = Coupling(name = 'GC_194',
	 value = '-1*complex(0,1)*(Vv51*(ZER31*complexconjugate(Ye11) + ZER32*complexconjugate(Ye21) + ZER33*complexconjugate(Ye31)) + Vv52*(ZER31*complexconjugate(Ye12) + ZER32*complexconjugate(Ye22) + ZER33*complexconjugate(Ye32)) + Vv53*(ZER31*complexconjugate(Ye13) + ZER32*complexconjugate(Ye23) + ZER33*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_195 = Coupling(name = 'GC_195',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66))*complexconjugate(ZEL11) + (Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66))*complexconjugate(ZEL12) + (Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66))*complexconjugate(ZEL13))', 
	 order = {'QED':1} ) 
 
GC_196 = Coupling(name = 'GC_196',
	 value = '-1*complex(0,1)*(Vv61*(ZER11*complexconjugate(Ye11) + ZER12*complexconjugate(Ye21) + ZER13*complexconjugate(Ye31)) + Vv62*(ZER11*complexconjugate(Ye12) + ZER12*complexconjugate(Ye22) + ZER13*complexconjugate(Ye32)) + Vv63*(ZER11*complexconjugate(Ye13) + ZER12*complexconjugate(Ye23) + ZER13*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_197 = Coupling(name = 'GC_197',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66))*complexconjugate(ZEL21) + (Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66))*complexconjugate(ZEL22) + (Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66))*complexconjugate(ZEL23))', 
	 order = {'QED':1} ) 
 
GC_198 = Coupling(name = 'GC_198',
	 value = '-1*complex(0,1)*(Vv61*(ZER21*complexconjugate(Ye11) + ZER22*complexconjugate(Ye21) + ZER23*complexconjugate(Ye31)) + Vv62*(ZER21*complexconjugate(Ye12) + ZER22*complexconjugate(Ye22) + ZER23*complexconjugate(Ye32)) + Vv63*(ZER21*complexconjugate(Ye13) + ZER22*complexconjugate(Ye23) + ZER23*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_199 = Coupling(name = 'GC_199',
	 value = '-1*complex(0,1)*((Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66))*complexconjugate(ZEL31) + (Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66))*complexconjugate(ZEL32) + (Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66))*complexconjugate(ZEL33))', 
	 order = {'QED':1} ) 
 
GC_200 = Coupling(name = 'GC_200',
	 value = '-1*complex(0,1)*(Vv61*(ZER31*complexconjugate(Ye11) + ZER32*complexconjugate(Ye21) + ZER33*complexconjugate(Ye31)) + Vv62*(ZER31*complexconjugate(Ye12) + ZER32*complexconjugate(Ye22) + ZER33*complexconjugate(Ye32)) + Vv63*(ZER31*complexconjugate(Ye13) + ZER32*complexconjugate(Ye23) + ZER33*complexconjugate(Ye33)))', 
	 order = {'QED':1} ) 
 
GC_201 = Coupling(name = 'GC_201',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL11)*(Ye11*complexconjugate(ZER11) + Ye21*complexconjugate(ZER12) + Ye31*complexconjugate(ZER13)) + complexconjugate(ZEL12)*(Ye12*complexconjugate(ZER11) + Ye22*complexconjugate(ZER12) + Ye32*complexconjugate(ZER13)) + complexconjugate(ZEL13)*(Ye13*complexconjugate(ZER11) + Ye23*complexconjugate(ZER12) + Ye33*complexconjugate(ZER13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_202 = Coupling(name = 'GC_202',
	 value = '(-1*complex(0,1)*(ZEL11*(ZER11*complexconjugate(Ye11) + ZER12*complexconjugate(Ye21) + ZER13*complexconjugate(Ye31)) + ZEL12*(ZER11*complexconjugate(Ye12) + ZER12*complexconjugate(Ye22) + ZER13*complexconjugate(Ye32)) + ZEL13*(ZER11*complexconjugate(Ye13) + ZER12*complexconjugate(Ye23) + ZER13*complexconjugate(Ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_203 = Coupling(name = 'GC_203',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL21)*(Ye11*complexconjugate(ZER11) + Ye21*complexconjugate(ZER12) + Ye31*complexconjugate(ZER13)) + complexconjugate(ZEL22)*(Ye12*complexconjugate(ZER11) + Ye22*complexconjugate(ZER12) + Ye32*complexconjugate(ZER13)) + complexconjugate(ZEL23)*(Ye13*complexconjugate(ZER11) + Ye23*complexconjugate(ZER12) + Ye33*complexconjugate(ZER13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_204 = Coupling(name = 'GC_204',
	 value = '(-1*complex(0,1)*(ZEL11*(ZER21*complexconjugate(Ye11) + ZER22*complexconjugate(Ye21) + ZER23*complexconjugate(Ye31)) + ZEL12*(ZER21*complexconjugate(Ye12) + ZER22*complexconjugate(Ye22) + ZER23*complexconjugate(Ye32)) + ZEL13*(ZER21*complexconjugate(Ye13) + ZER22*complexconjugate(Ye23) + ZER23*complexconjugate(Ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_205 = Coupling(name = 'GC_205',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL31)*(Ye11*complexconjugate(ZER11) + Ye21*complexconjugate(ZER12) + Ye31*complexconjugate(ZER13)) + complexconjugate(ZEL32)*(Ye12*complexconjugate(ZER11) + Ye22*complexconjugate(ZER12) + Ye32*complexconjugate(ZER13)) + complexconjugate(ZEL33)*(Ye13*complexconjugate(ZER11) + Ye23*complexconjugate(ZER12) + Ye33*complexconjugate(ZER13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_206 = Coupling(name = 'GC_206',
	 value = '(-1*complex(0,1)*(ZEL11*(ZER31*complexconjugate(Ye11) + ZER32*complexconjugate(Ye21) + ZER33*complexconjugate(Ye31)) + ZEL12*(ZER31*complexconjugate(Ye12) + ZER32*complexconjugate(Ye22) + ZER33*complexconjugate(Ye32)) + ZEL13*(ZER31*complexconjugate(Ye13) + ZER32*complexconjugate(Ye23) + ZER33*complexconjugate(Ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_207 = Coupling(name = 'GC_207',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL11)*(Ye11*complexconjugate(ZER21) + Ye21*complexconjugate(ZER22) + Ye31*complexconjugate(ZER23)) + complexconjugate(ZEL12)*(Ye12*complexconjugate(ZER21) + Ye22*complexconjugate(ZER22) + Ye32*complexconjugate(ZER23)) + complexconjugate(ZEL13)*(Ye13*complexconjugate(ZER21) + Ye23*complexconjugate(ZER22) + Ye33*complexconjugate(ZER23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_208 = Coupling(name = 'GC_208',
	 value = '(-1*complex(0,1)*(ZEL21*(ZER11*complexconjugate(Ye11) + ZER12*complexconjugate(Ye21) + ZER13*complexconjugate(Ye31)) + ZEL22*(ZER11*complexconjugate(Ye12) + ZER12*complexconjugate(Ye22) + ZER13*complexconjugate(Ye32)) + ZEL23*(ZER11*complexconjugate(Ye13) + ZER12*complexconjugate(Ye23) + ZER13*complexconjugate(Ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_209 = Coupling(name = 'GC_209',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL21)*(Ye11*complexconjugate(ZER21) + Ye21*complexconjugate(ZER22) + Ye31*complexconjugate(ZER23)) + complexconjugate(ZEL22)*(Ye12*complexconjugate(ZER21) + Ye22*complexconjugate(ZER22) + Ye32*complexconjugate(ZER23)) + complexconjugate(ZEL23)*(Ye13*complexconjugate(ZER21) + Ye23*complexconjugate(ZER22) + Ye33*complexconjugate(ZER23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_210 = Coupling(name = 'GC_210',
	 value = '(-1*complex(0,1)*(ZEL21*(ZER21*complexconjugate(Ye11) + ZER22*complexconjugate(Ye21) + ZER23*complexconjugate(Ye31)) + ZEL22*(ZER21*complexconjugate(Ye12) + ZER22*complexconjugate(Ye22) + ZER23*complexconjugate(Ye32)) + ZEL23*(ZER21*complexconjugate(Ye13) + ZER22*complexconjugate(Ye23) + ZER23*complexconjugate(Ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_211 = Coupling(name = 'GC_211',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL31)*(Ye11*complexconjugate(ZER21) + Ye21*complexconjugate(ZER22) + Ye31*complexconjugate(ZER23)) + complexconjugate(ZEL32)*(Ye12*complexconjugate(ZER21) + Ye22*complexconjugate(ZER22) + Ye32*complexconjugate(ZER23)) + complexconjugate(ZEL33)*(Ye13*complexconjugate(ZER21) + Ye23*complexconjugate(ZER22) + Ye33*complexconjugate(ZER23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_212 = Coupling(name = 'GC_212',
	 value = '(-1*complex(0,1)*(ZEL21*(ZER31*complexconjugate(Ye11) + ZER32*complexconjugate(Ye21) + ZER33*complexconjugate(Ye31)) + ZEL22*(ZER31*complexconjugate(Ye12) + ZER32*complexconjugate(Ye22) + ZER33*complexconjugate(Ye32)) + ZEL23*(ZER31*complexconjugate(Ye13) + ZER32*complexconjugate(Ye23) + ZER33*complexconjugate(Ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_213 = Coupling(name = 'GC_213',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL11)*(Ye11*complexconjugate(ZER31) + Ye21*complexconjugate(ZER32) + Ye31*complexconjugate(ZER33)) + complexconjugate(ZEL12)*(Ye12*complexconjugate(ZER31) + Ye22*complexconjugate(ZER32) + Ye32*complexconjugate(ZER33)) + complexconjugate(ZEL13)*(Ye13*complexconjugate(ZER31) + Ye23*complexconjugate(ZER32) + Ye33*complexconjugate(ZER33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_214 = Coupling(name = 'GC_214',
	 value = '(-1*complex(0,1)*(ZEL31*(ZER11*complexconjugate(Ye11) + ZER12*complexconjugate(Ye21) + ZER13*complexconjugate(Ye31)) + ZEL32*(ZER11*complexconjugate(Ye12) + ZER12*complexconjugate(Ye22) + ZER13*complexconjugate(Ye32)) + ZEL33*(ZER11*complexconjugate(Ye13) + ZER12*complexconjugate(Ye23) + ZER13*complexconjugate(Ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_215 = Coupling(name = 'GC_215',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL21)*(Ye11*complexconjugate(ZER31) + Ye21*complexconjugate(ZER32) + Ye31*complexconjugate(ZER33)) + complexconjugate(ZEL22)*(Ye12*complexconjugate(ZER31) + Ye22*complexconjugate(ZER32) + Ye32*complexconjugate(ZER33)) + complexconjugate(ZEL23)*(Ye13*complexconjugate(ZER31) + Ye23*complexconjugate(ZER32) + Ye33*complexconjugate(ZER33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_216 = Coupling(name = 'GC_216',
	 value = '(-1*complex(0,1)*(ZEL31*(ZER21*complexconjugate(Ye11) + ZER22*complexconjugate(Ye21) + ZER23*complexconjugate(Ye31)) + ZEL32*(ZER21*complexconjugate(Ye12) + ZER22*complexconjugate(Ye22) + ZER23*complexconjugate(Ye32)) + ZEL33*(ZER21*complexconjugate(Ye13) + ZER22*complexconjugate(Ye23) + ZER23*complexconjugate(Ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_217 = Coupling(name = 'GC_217',
	 value = '(-1*complex(0,1)*(complexconjugate(ZEL31)*(Ye11*complexconjugate(ZER31) + Ye21*complexconjugate(ZER32) + Ye31*complexconjugate(ZER33)) + complexconjugate(ZEL32)*(Ye12*complexconjugate(ZER31) + Ye22*complexconjugate(ZER32) + Ye32*complexconjugate(ZER33)) + complexconjugate(ZEL33)*(Ye13*complexconjugate(ZER31) + Ye23*complexconjugate(ZER32) + Ye33*complexconjugate(ZER33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_218 = Coupling(name = 'GC_218',
	 value = '(-1*complex(0,1)*(ZEL31*(ZER31*complexconjugate(Ye11) + ZER32*complexconjugate(Ye21) + ZER33*complexconjugate(Ye31)) + ZEL32*(ZER31*complexconjugate(Ye12) + ZER32*complexconjugate(Ye22) + ZER33*complexconjugate(Ye32)) + ZEL33*(ZER31*complexconjugate(Ye13) + ZER32*complexconjugate(Ye23) + ZER33*complexconjugate(Ye33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_219 = Coupling(name = 'GC_219',
	 value = '(1*complex(0,1)*(complexconjugate(ZUL11)*(Yu11*complexconjugate(ZUR11) + Yu21*complexconjugate(ZUR12) + Yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL12)*(Yu12*complexconjugate(ZUR11) + Yu22*complexconjugate(ZUR12) + Yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL13)*(Yu13*complexconjugate(ZUR11) + Yu23*complexconjugate(ZUR12) + Yu33*complexconjugate(ZUR13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_220 = Coupling(name = 'GC_220',
	 value = '(1*complex(0,1)*(ZUL11*(ZUR11*complexconjugate(Yu11) + ZUR12*complexconjugate(Yu21) + ZUR13*complexconjugate(Yu31)) + ZUL12*(ZUR11*complexconjugate(Yu12) + ZUR12*complexconjugate(Yu22) + ZUR13*complexconjugate(Yu32)) + ZUL13*(ZUR11*complexconjugate(Yu13) + ZUR12*complexconjugate(Yu23) + ZUR13*complexconjugate(Yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_221 = Coupling(name = 'GC_221',
	 value = '(1*complex(0,1)*(complexconjugate(ZUL21)*(Yu11*complexconjugate(ZUR11) + Yu21*complexconjugate(ZUR12) + Yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL22)*(Yu12*complexconjugate(ZUR11) + Yu22*complexconjugate(ZUR12) + Yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL23)*(Yu13*complexconjugate(ZUR11) + Yu23*complexconjugate(ZUR12) + Yu33*complexconjugate(ZUR13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_222 = Coupling(name = 'GC_222',
	 value = '(1*complex(0,1)*(ZUL11*(ZUR21*complexconjugate(Yu11) + ZUR22*complexconjugate(Yu21) + ZUR23*complexconjugate(Yu31)) + ZUL12*(ZUR21*complexconjugate(Yu12) + ZUR22*complexconjugate(Yu22) + ZUR23*complexconjugate(Yu32)) + ZUL13*(ZUR21*complexconjugate(Yu13) + ZUR22*complexconjugate(Yu23) + ZUR23*complexconjugate(Yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_223 = Coupling(name = 'GC_223',
	 value = '(1*complex(0,1)*(complexconjugate(ZUL31)*(Yu11*complexconjugate(ZUR11) + Yu21*complexconjugate(ZUR12) + Yu31*complexconjugate(ZUR13)) + complexconjugate(ZUL32)*(Yu12*complexconjugate(ZUR11) + Yu22*complexconjugate(ZUR12) + Yu32*complexconjugate(ZUR13)) + complexconjugate(ZUL33)*(Yu13*complexconjugate(ZUR11) + Yu23*complexconjugate(ZUR12) + Yu33*complexconjugate(ZUR13))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_224 = Coupling(name = 'GC_224',
	 value = '(1*complex(0,1)*(ZUL11*(ZUR31*complexconjugate(Yu11) + ZUR32*complexconjugate(Yu21) + ZUR33*complexconjugate(Yu31)) + ZUL12*(ZUR31*complexconjugate(Yu12) + ZUR32*complexconjugate(Yu22) + ZUR33*complexconjugate(Yu32)) + ZUL13*(ZUR31*complexconjugate(Yu13) + ZUR32*complexconjugate(Yu23) + ZUR33*complexconjugate(Yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_225 = Coupling(name = 'GC_225',
	 value = '(1*complex(0,1)*(complexconjugate(ZUL11)*(Yu11*complexconjugate(ZUR21) + Yu21*complexconjugate(ZUR22) + Yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL12)*(Yu12*complexconjugate(ZUR21) + Yu22*complexconjugate(ZUR22) + Yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL13)*(Yu13*complexconjugate(ZUR21) + Yu23*complexconjugate(ZUR22) + Yu33*complexconjugate(ZUR23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_226 = Coupling(name = 'GC_226',
	 value = '(1*complex(0,1)*(ZUL21*(ZUR11*complexconjugate(Yu11) + ZUR12*complexconjugate(Yu21) + ZUR13*complexconjugate(Yu31)) + ZUL22*(ZUR11*complexconjugate(Yu12) + ZUR12*complexconjugate(Yu22) + ZUR13*complexconjugate(Yu32)) + ZUL23*(ZUR11*complexconjugate(Yu13) + ZUR12*complexconjugate(Yu23) + ZUR13*complexconjugate(Yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_227 = Coupling(name = 'GC_227',
	 value = '(1*complex(0,1)*(complexconjugate(ZUL21)*(Yu11*complexconjugate(ZUR21) + Yu21*complexconjugate(ZUR22) + Yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL22)*(Yu12*complexconjugate(ZUR21) + Yu22*complexconjugate(ZUR22) + Yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL23)*(Yu13*complexconjugate(ZUR21) + Yu23*complexconjugate(ZUR22) + Yu33*complexconjugate(ZUR23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_228 = Coupling(name = 'GC_228',
	 value = '(1*complex(0,1)*(ZUL21*(ZUR21*complexconjugate(Yu11) + ZUR22*complexconjugate(Yu21) + ZUR23*complexconjugate(Yu31)) + ZUL22*(ZUR21*complexconjugate(Yu12) + ZUR22*complexconjugate(Yu22) + ZUR23*complexconjugate(Yu32)) + ZUL23*(ZUR21*complexconjugate(Yu13) + ZUR22*complexconjugate(Yu23) + ZUR23*complexconjugate(Yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_229 = Coupling(name = 'GC_229',
	 value = '(1*complex(0,1)*(complexconjugate(ZUL31)*(Yu11*complexconjugate(ZUR21) + Yu21*complexconjugate(ZUR22) + Yu31*complexconjugate(ZUR23)) + complexconjugate(ZUL32)*(Yu12*complexconjugate(ZUR21) + Yu22*complexconjugate(ZUR22) + Yu32*complexconjugate(ZUR23)) + complexconjugate(ZUL33)*(Yu13*complexconjugate(ZUR21) + Yu23*complexconjugate(ZUR22) + Yu33*complexconjugate(ZUR23))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_230 = Coupling(name = 'GC_230',
	 value = '(1*complex(0,1)*(ZUL21*(ZUR31*complexconjugate(Yu11) + ZUR32*complexconjugate(Yu21) + ZUR33*complexconjugate(Yu31)) + ZUL22*(ZUR31*complexconjugate(Yu12) + ZUR32*complexconjugate(Yu22) + ZUR33*complexconjugate(Yu32)) + ZUL23*(ZUR31*complexconjugate(Yu13) + ZUR32*complexconjugate(Yu23) + ZUR33*complexconjugate(Yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_231 = Coupling(name = 'GC_231',
	 value = '(1*complex(0,1)*(complexconjugate(ZUL11)*(Yu11*complexconjugate(ZUR31) + Yu21*complexconjugate(ZUR32) + Yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL12)*(Yu12*complexconjugate(ZUR31) + Yu22*complexconjugate(ZUR32) + Yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL13)*(Yu13*complexconjugate(ZUR31) + Yu23*complexconjugate(ZUR32) + Yu33*complexconjugate(ZUR33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_232 = Coupling(name = 'GC_232',
	 value = '(1*complex(0,1)*(ZUL31*(ZUR11*complexconjugate(Yu11) + ZUR12*complexconjugate(Yu21) + ZUR13*complexconjugate(Yu31)) + ZUL32*(ZUR11*complexconjugate(Yu12) + ZUR12*complexconjugate(Yu22) + ZUR13*complexconjugate(Yu32)) + ZUL33*(ZUR11*complexconjugate(Yu13) + ZUR12*complexconjugate(Yu23) + ZUR13*complexconjugate(Yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_233 = Coupling(name = 'GC_233',
	 value = '(1*complex(0,1)*(complexconjugate(ZUL21)*(Yu11*complexconjugate(ZUR31) + Yu21*complexconjugate(ZUR32) + Yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL22)*(Yu12*complexconjugate(ZUR31) + Yu22*complexconjugate(ZUR32) + Yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL23)*(Yu13*complexconjugate(ZUR31) + Yu23*complexconjugate(ZUR32) + Yu33*complexconjugate(ZUR33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_234 = Coupling(name = 'GC_234',
	 value = '(1*complex(0,1)*(ZUL31*(ZUR21*complexconjugate(Yu11) + ZUR22*complexconjugate(Yu21) + ZUR23*complexconjugate(Yu31)) + ZUL32*(ZUR21*complexconjugate(Yu12) + ZUR22*complexconjugate(Yu22) + ZUR23*complexconjugate(Yu32)) + ZUL33*(ZUR21*complexconjugate(Yu13) + ZUR22*complexconjugate(Yu23) + ZUR23*complexconjugate(Yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_235 = Coupling(name = 'GC_235',
	 value = '(1*complex(0,1)*(complexconjugate(ZUL31)*(Yu11*complexconjugate(ZUR31) + Yu21*complexconjugate(ZUR32) + Yu31*complexconjugate(ZUR33)) + complexconjugate(ZUL32)*(Yu12*complexconjugate(ZUR31) + Yu22*complexconjugate(ZUR32) + Yu32*complexconjugate(ZUR33)) + complexconjugate(ZUL33)*(Yu13*complexconjugate(ZUR31) + Yu23*complexconjugate(ZUR32) + Yu33*complexconjugate(ZUR33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_236 = Coupling(name = 'GC_236',
	 value = '(1*complex(0,1)*(ZUL31*(ZUR31*complexconjugate(Yu11) + ZUR32*complexconjugate(Yu21) + ZUR33*complexconjugate(Yu31)) + ZUL32*(ZUR31*complexconjugate(Yu12) + ZUR32*complexconjugate(Yu22) + ZUR33*complexconjugate(Yu32)) + ZUL33*(ZUR31*complexconjugate(Yu13) + ZUR32*complexconjugate(Yu23) + ZUR33*complexconjugate(Yu33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_237 = Coupling(name = 'GC_237',
	 value = '-1*complex(0,1)*((Yd11*complexconjugate(ZDR11) + Yd21*complexconjugate(ZDR12) + Yd31*complexconjugate(ZDR13))*complexconjugate(ZUL11) + (Yd12*complexconjugate(ZDR11) + Yd22*complexconjugate(ZDR12) + Yd32*complexconjugate(ZDR13))*complexconjugate(ZUL12) + (Yd13*complexconjugate(ZDR11) + Yd23*complexconjugate(ZDR12) + Yd33*complexconjugate(ZDR13))*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_238 = Coupling(name = 'GC_238',
	 value = '-1*complex(0,1)*(ZDL11*(ZUR11*complexconjugate(Yu11) + ZUR12*complexconjugate(Yu21) + ZUR13*complexconjugate(Yu31)) + ZDL12*(ZUR11*complexconjugate(Yu12) + ZUR12*complexconjugate(Yu22) + ZUR13*complexconjugate(Yu32)) + ZDL13*(ZUR11*complexconjugate(Yu13) + ZUR12*complexconjugate(Yu23) + ZUR13*complexconjugate(Yu33)))', 
	 order = {'QED':1} ) 
 
GC_239 = Coupling(name = 'GC_239',
	 value = '-1*complex(0,1)*((Yd11*complexconjugate(ZDR11) + Yd21*complexconjugate(ZDR12) + Yd31*complexconjugate(ZDR13))*complexconjugate(ZUL21) + (Yd12*complexconjugate(ZDR11) + Yd22*complexconjugate(ZDR12) + Yd32*complexconjugate(ZDR13))*complexconjugate(ZUL22) + (Yd13*complexconjugate(ZDR11) + Yd23*complexconjugate(ZDR12) + Yd33*complexconjugate(ZDR13))*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_240 = Coupling(name = 'GC_240',
	 value = '-1*complex(0,1)*(ZDL11*(ZUR21*complexconjugate(Yu11) + ZUR22*complexconjugate(Yu21) + ZUR23*complexconjugate(Yu31)) + ZDL12*(ZUR21*complexconjugate(Yu12) + ZUR22*complexconjugate(Yu22) + ZUR23*complexconjugate(Yu32)) + ZDL13*(ZUR21*complexconjugate(Yu13) + ZUR22*complexconjugate(Yu23) + ZUR23*complexconjugate(Yu33)))', 
	 order = {'QED':1} ) 
 
GC_241 = Coupling(name = 'GC_241',
	 value = '-1*complex(0,1)*((Yd11*complexconjugate(ZDR11) + Yd21*complexconjugate(ZDR12) + Yd31*complexconjugate(ZDR13))*complexconjugate(ZUL31) + (Yd12*complexconjugate(ZDR11) + Yd22*complexconjugate(ZDR12) + Yd32*complexconjugate(ZDR13))*complexconjugate(ZUL32) + (Yd13*complexconjugate(ZDR11) + Yd23*complexconjugate(ZDR12) + Yd33*complexconjugate(ZDR13))*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_242 = Coupling(name = 'GC_242',
	 value = '-1*complex(0,1)*(ZDL11*(ZUR31*complexconjugate(Yu11) + ZUR32*complexconjugate(Yu21) + ZUR33*complexconjugate(Yu31)) + ZDL12*(ZUR31*complexconjugate(Yu12) + ZUR32*complexconjugate(Yu22) + ZUR33*complexconjugate(Yu32)) + ZDL13*(ZUR31*complexconjugate(Yu13) + ZUR32*complexconjugate(Yu23) + ZUR33*complexconjugate(Yu33)))', 
	 order = {'QED':1} ) 
 
GC_243 = Coupling(name = 'GC_243',
	 value = '-1*complex(0,1)*((Yd11*complexconjugate(ZDR21) + Yd21*complexconjugate(ZDR22) + Yd31*complexconjugate(ZDR23))*complexconjugate(ZUL11) + (Yd12*complexconjugate(ZDR21) + Yd22*complexconjugate(ZDR22) + Yd32*complexconjugate(ZDR23))*complexconjugate(ZUL12) + (Yd13*complexconjugate(ZDR21) + Yd23*complexconjugate(ZDR22) + Yd33*complexconjugate(ZDR23))*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_244 = Coupling(name = 'GC_244',
	 value = '-1*complex(0,1)*(ZDL21*(ZUR11*complexconjugate(Yu11) + ZUR12*complexconjugate(Yu21) + ZUR13*complexconjugate(Yu31)) + ZDL22*(ZUR11*complexconjugate(Yu12) + ZUR12*complexconjugate(Yu22) + ZUR13*complexconjugate(Yu32)) + ZDL23*(ZUR11*complexconjugate(Yu13) + ZUR12*complexconjugate(Yu23) + ZUR13*complexconjugate(Yu33)))', 
	 order = {'QED':1} ) 
 
GC_245 = Coupling(name = 'GC_245',
	 value = '-1*complex(0,1)*((Yd11*complexconjugate(ZDR21) + Yd21*complexconjugate(ZDR22) + Yd31*complexconjugate(ZDR23))*complexconjugate(ZUL21) + (Yd12*complexconjugate(ZDR21) + Yd22*complexconjugate(ZDR22) + Yd32*complexconjugate(ZDR23))*complexconjugate(ZUL22) + (Yd13*complexconjugate(ZDR21) + Yd23*complexconjugate(ZDR22) + Yd33*complexconjugate(ZDR23))*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_246 = Coupling(name = 'GC_246',
	 value = '-1*complex(0,1)*(ZDL21*(ZUR21*complexconjugate(Yu11) + ZUR22*complexconjugate(Yu21) + ZUR23*complexconjugate(Yu31)) + ZDL22*(ZUR21*complexconjugate(Yu12) + ZUR22*complexconjugate(Yu22) + ZUR23*complexconjugate(Yu32)) + ZDL23*(ZUR21*complexconjugate(Yu13) + ZUR22*complexconjugate(Yu23) + ZUR23*complexconjugate(Yu33)))', 
	 order = {'QED':1} ) 
 
GC_247 = Coupling(name = 'GC_247',
	 value = '-1*complex(0,1)*((Yd11*complexconjugate(ZDR21) + Yd21*complexconjugate(ZDR22) + Yd31*complexconjugate(ZDR23))*complexconjugate(ZUL31) + (Yd12*complexconjugate(ZDR21) + Yd22*complexconjugate(ZDR22) + Yd32*complexconjugate(ZDR23))*complexconjugate(ZUL32) + (Yd13*complexconjugate(ZDR21) + Yd23*complexconjugate(ZDR22) + Yd33*complexconjugate(ZDR23))*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_248 = Coupling(name = 'GC_248',
	 value = '-1*complex(0,1)*(ZDL21*(ZUR31*complexconjugate(Yu11) + ZUR32*complexconjugate(Yu21) + ZUR33*complexconjugate(Yu31)) + ZDL22*(ZUR31*complexconjugate(Yu12) + ZUR32*complexconjugate(Yu22) + ZUR33*complexconjugate(Yu32)) + ZDL23*(ZUR31*complexconjugate(Yu13) + ZUR32*complexconjugate(Yu23) + ZUR33*complexconjugate(Yu33)))', 
	 order = {'QED':1} ) 
 
GC_249 = Coupling(name = 'GC_249',
	 value = '-1*complex(0,1)*((Yd11*complexconjugate(ZDR31) + Yd21*complexconjugate(ZDR32) + Yd31*complexconjugate(ZDR33))*complexconjugate(ZUL11) + (Yd12*complexconjugate(ZDR31) + Yd22*complexconjugate(ZDR32) + Yd32*complexconjugate(ZDR33))*complexconjugate(ZUL12) + (Yd13*complexconjugate(ZDR31) + Yd23*complexconjugate(ZDR32) + Yd33*complexconjugate(ZDR33))*complexconjugate(ZUL13))', 
	 order = {'QED':1} ) 
 
GC_250 = Coupling(name = 'GC_250',
	 value = '-1*complex(0,1)*(ZDL31*(ZUR11*complexconjugate(Yu11) + ZUR12*complexconjugate(Yu21) + ZUR13*complexconjugate(Yu31)) + ZDL32*(ZUR11*complexconjugate(Yu12) + ZUR12*complexconjugate(Yu22) + ZUR13*complexconjugate(Yu32)) + ZDL33*(ZUR11*complexconjugate(Yu13) + ZUR12*complexconjugate(Yu23) + ZUR13*complexconjugate(Yu33)))', 
	 order = {'QED':1} ) 
 
GC_251 = Coupling(name = 'GC_251',
	 value = '-1*complex(0,1)*((Yd11*complexconjugate(ZDR31) + Yd21*complexconjugate(ZDR32) + Yd31*complexconjugate(ZDR33))*complexconjugate(ZUL21) + (Yd12*complexconjugate(ZDR31) + Yd22*complexconjugate(ZDR32) + Yd32*complexconjugate(ZDR33))*complexconjugate(ZUL22) + (Yd13*complexconjugate(ZDR31) + Yd23*complexconjugate(ZDR32) + Yd33*complexconjugate(ZDR33))*complexconjugate(ZUL23))', 
	 order = {'QED':1} ) 
 
GC_252 = Coupling(name = 'GC_252',
	 value = '-1*complex(0,1)*(ZDL31*(ZUR21*complexconjugate(Yu11) + ZUR22*complexconjugate(Yu21) + ZUR23*complexconjugate(Yu31)) + ZDL32*(ZUR21*complexconjugate(Yu12) + ZUR22*complexconjugate(Yu22) + ZUR23*complexconjugate(Yu32)) + ZDL33*(ZUR21*complexconjugate(Yu13) + ZUR22*complexconjugate(Yu23) + ZUR23*complexconjugate(Yu33)))', 
	 order = {'QED':1} ) 
 
GC_253 = Coupling(name = 'GC_253',
	 value = '-1*complex(0,1)*((Yd11*complexconjugate(ZDR31) + Yd21*complexconjugate(ZDR32) + Yd31*complexconjugate(ZDR33))*complexconjugate(ZUL31) + (Yd12*complexconjugate(ZDR31) + Yd22*complexconjugate(ZDR32) + Yd32*complexconjugate(ZDR33))*complexconjugate(ZUL32) + (Yd13*complexconjugate(ZDR31) + Yd23*complexconjugate(ZDR32) + Yd33*complexconjugate(ZDR33))*complexconjugate(ZUL33))', 
	 order = {'QED':1} ) 
 
GC_254 = Coupling(name = 'GC_254',
	 value = '-1*complex(0,1)*(ZDL31*(ZUR31*complexconjugate(Yu11) + ZUR32*complexconjugate(Yu21) + ZUR33*complexconjugate(Yu31)) + ZDL32*(ZUR31*complexconjugate(Yu12) + ZUR32*complexconjugate(Yu22) + ZUR33*complexconjugate(Yu32)) + ZDL33*(ZUR31*complexconjugate(Yu13) + ZUR32*complexconjugate(Yu23) + ZUR33*complexconjugate(Yu33)))', 
	 order = {'QED':1} ) 
 
GC_255 = Coupling(name = 'GC_255',
	 value = '(1*complex(0,1)*(2*complexconjugate(Vv11)*(Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16)) + 2*complexconjugate(Vv12)*(Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16)) + 2*complexconjugate(Vv13)*(Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_256 = Coupling(name = 'GC_256',
	 value = '(1*complex(0,1)*(2*Vv11*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + 2*Vv12*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + 2*Vv13*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_257 = Coupling(name = 'GC_257',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(Vv21) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(Vv22) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(Vv23) + complexconjugate(Vv11)*(Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26)) + complexconjugate(Vv12)*(Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26)) + complexconjugate(Vv13)*(Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_258 = Coupling(name = 'GC_258',
	 value = '(1*complex(0,1)*(Vv21*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + Vv11*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + Vv22*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + Vv12*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + Vv23*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)) + Vv13*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_259 = Coupling(name = 'GC_259',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(Vv31) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(Vv32) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(Vv33) + complexconjugate(Vv11)*(Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36)) + complexconjugate(Vv12)*(Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36)) + complexconjugate(Vv13)*(Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_260 = Coupling(name = 'GC_260',
	 value = '(1*complex(0,1)*(Vv31*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + Vv11*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + Vv32*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + Vv12*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + Vv33*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)) + Vv13*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_261 = Coupling(name = 'GC_261',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(Vv41) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(Vv42) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(Vv43) + complexconjugate(Vv11)*(Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46)) + complexconjugate(Vv12)*(Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46)) + complexconjugate(Vv13)*(Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_262 = Coupling(name = 'GC_262',
	 value = '(1*complex(0,1)*(Vv41*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + Vv11*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + Vv42*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + Vv12*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + Vv43*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)) + Vv13*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_263 = Coupling(name = 'GC_263',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(Vv51) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(Vv52) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(Vv53) + complexconjugate(Vv11)*(Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56)) + complexconjugate(Vv12)*(Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56)) + complexconjugate(Vv13)*(Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_264 = Coupling(name = 'GC_264',
	 value = '(1*complex(0,1)*(Vv51*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + Vv11*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + Vv52*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + Vv12*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + Vv53*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)) + Vv13*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_265 = Coupling(name = 'GC_265',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv14) + Yv21*complexconjugate(Vv15) + Yv31*complexconjugate(Vv16))*complexconjugate(Vv61) + (Yv12*complexconjugate(Vv14) + Yv22*complexconjugate(Vv15) + Yv32*complexconjugate(Vv16))*complexconjugate(Vv62) + (Yv13*complexconjugate(Vv14) + Yv23*complexconjugate(Vv15) + Yv33*complexconjugate(Vv16))*complexconjugate(Vv63) + complexconjugate(Vv11)*(Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66)) + complexconjugate(Vv12)*(Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66)) + complexconjugate(Vv13)*(Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_266 = Coupling(name = 'GC_266',
	 value = '(1*complex(0,1)*(Vv61*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + Vv11*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + Vv62*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + Vv12*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + Vv63*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)) + Vv13*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_267 = Coupling(name = 'GC_267',
	 value = '(1*complex(0,1)*(2*complexconjugate(Vv21)*(Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26)) + 2*complexconjugate(Vv22)*(Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26)) + 2*complexconjugate(Vv23)*(Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_268 = Coupling(name = 'GC_268',
	 value = '(1*complex(0,1)*(2*Vv21*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + 2*Vv22*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + 2*Vv23*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_269 = Coupling(name = 'GC_269',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26))*complexconjugate(Vv31) + (Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26))*complexconjugate(Vv32) + (Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))*complexconjugate(Vv33) + complexconjugate(Vv21)*(Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36)) + complexconjugate(Vv22)*(Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36)) + complexconjugate(Vv23)*(Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_270 = Coupling(name = 'GC_270',
	 value = '(1*complex(0,1)*(Vv31*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + Vv21*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + Vv32*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + Vv22*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + Vv33*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)) + Vv23*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_271 = Coupling(name = 'GC_271',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26))*complexconjugate(Vv41) + (Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26))*complexconjugate(Vv42) + (Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))*complexconjugate(Vv43) + complexconjugate(Vv21)*(Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46)) + complexconjugate(Vv22)*(Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46)) + complexconjugate(Vv23)*(Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_272 = Coupling(name = 'GC_272',
	 value = '(1*complex(0,1)*(Vv41*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + Vv21*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + Vv42*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + Vv22*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + Vv43*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)) + Vv23*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_273 = Coupling(name = 'GC_273',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26))*complexconjugate(Vv51) + (Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26))*complexconjugate(Vv52) + (Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))*complexconjugate(Vv53) + complexconjugate(Vv21)*(Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56)) + complexconjugate(Vv22)*(Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56)) + complexconjugate(Vv23)*(Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_274 = Coupling(name = 'GC_274',
	 value = '(1*complex(0,1)*(Vv51*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + Vv21*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + Vv52*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + Vv22*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + Vv53*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)) + Vv23*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_275 = Coupling(name = 'GC_275',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv24) + Yv21*complexconjugate(Vv25) + Yv31*complexconjugate(Vv26))*complexconjugate(Vv61) + (Yv12*complexconjugate(Vv24) + Yv22*complexconjugate(Vv25) + Yv32*complexconjugate(Vv26))*complexconjugate(Vv62) + (Yv13*complexconjugate(Vv24) + Yv23*complexconjugate(Vv25) + Yv33*complexconjugate(Vv26))*complexconjugate(Vv63) + complexconjugate(Vv21)*(Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66)) + complexconjugate(Vv22)*(Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66)) + complexconjugate(Vv23)*(Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_276 = Coupling(name = 'GC_276',
	 value = '(1*complex(0,1)*(Vv61*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + Vv21*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + Vv62*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + Vv22*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + Vv63*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)) + Vv23*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_277 = Coupling(name = 'GC_277',
	 value = '(1*complex(0,1)*(2*complexconjugate(Vv31)*(Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36)) + 2*complexconjugate(Vv32)*(Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36)) + 2*complexconjugate(Vv33)*(Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_278 = Coupling(name = 'GC_278',
	 value = '(1*complex(0,1)*(2*Vv31*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + 2*Vv32*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + 2*Vv33*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_279 = Coupling(name = 'GC_279',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36))*complexconjugate(Vv41) + (Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36))*complexconjugate(Vv42) + (Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36))*complexconjugate(Vv43) + complexconjugate(Vv31)*(Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46)) + complexconjugate(Vv32)*(Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46)) + complexconjugate(Vv33)*(Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_280 = Coupling(name = 'GC_280',
	 value = '(1*complex(0,1)*(Vv41*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + Vv31*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + Vv42*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + Vv32*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + Vv43*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33)) + Vv33*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_281 = Coupling(name = 'GC_281',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36))*complexconjugate(Vv51) + (Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36))*complexconjugate(Vv52) + (Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36))*complexconjugate(Vv53) + complexconjugate(Vv31)*(Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56)) + complexconjugate(Vv32)*(Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56)) + complexconjugate(Vv33)*(Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_282 = Coupling(name = 'GC_282',
	 value = '(1*complex(0,1)*(Vv51*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + Vv31*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + Vv52*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + Vv32*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + Vv53*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33)) + Vv33*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_283 = Coupling(name = 'GC_283',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv34) + Yv21*complexconjugate(Vv35) + Yv31*complexconjugate(Vv36))*complexconjugate(Vv61) + (Yv12*complexconjugate(Vv34) + Yv22*complexconjugate(Vv35) + Yv32*complexconjugate(Vv36))*complexconjugate(Vv62) + (Yv13*complexconjugate(Vv34) + Yv23*complexconjugate(Vv35) + Yv33*complexconjugate(Vv36))*complexconjugate(Vv63) + complexconjugate(Vv31)*(Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66)) + complexconjugate(Vv32)*(Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66)) + complexconjugate(Vv33)*(Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_284 = Coupling(name = 'GC_284',
	 value = '(1*complex(0,1)*(Vv61*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + Vv31*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + Vv62*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + Vv32*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + Vv63*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33)) + Vv33*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_285 = Coupling(name = 'GC_285',
	 value = '(1*complex(0,1)*(2*complexconjugate(Vv41)*(Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46)) + 2*complexconjugate(Vv42)*(Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46)) + 2*complexconjugate(Vv43)*(Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_286 = Coupling(name = 'GC_286',
	 value = '(1*complex(0,1)*(2*Vv41*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + 2*Vv42*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + 2*Vv43*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_287 = Coupling(name = 'GC_287',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46))*complexconjugate(Vv51) + (Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46))*complexconjugate(Vv52) + (Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46))*complexconjugate(Vv53) + complexconjugate(Vv41)*(Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56)) + complexconjugate(Vv42)*(Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56)) + complexconjugate(Vv43)*(Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_288 = Coupling(name = 'GC_288',
	 value = '(1*complex(0,1)*(Vv51*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + Vv41*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + Vv52*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + Vv42*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + Vv53*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33)) + Vv43*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_289 = Coupling(name = 'GC_289',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv44) + Yv21*complexconjugate(Vv45) + Yv31*complexconjugate(Vv46))*complexconjugate(Vv61) + (Yv12*complexconjugate(Vv44) + Yv22*complexconjugate(Vv45) + Yv32*complexconjugate(Vv46))*complexconjugate(Vv62) + (Yv13*complexconjugate(Vv44) + Yv23*complexconjugate(Vv45) + Yv33*complexconjugate(Vv46))*complexconjugate(Vv63) + complexconjugate(Vv41)*(Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66)) + complexconjugate(Vv42)*(Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66)) + complexconjugate(Vv43)*(Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_290 = Coupling(name = 'GC_290',
	 value = '(1*complex(0,1)*(Vv61*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + Vv41*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + Vv62*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + Vv42*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + Vv63*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33)) + Vv43*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_291 = Coupling(name = 'GC_291',
	 value = '(1*complex(0,1)*(2*complexconjugate(Vv51)*(Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56)) + 2*complexconjugate(Vv52)*(Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56)) + 2*complexconjugate(Vv53)*(Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_292 = Coupling(name = 'GC_292',
	 value = '(1*complex(0,1)*(2*Vv51*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + 2*Vv52*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + 2*Vv53*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_293 = Coupling(name = 'GC_293',
	 value = '(1*complex(0,1)*((Yv11*complexconjugate(Vv54) + Yv21*complexconjugate(Vv55) + Yv31*complexconjugate(Vv56))*complexconjugate(Vv61) + (Yv12*complexconjugate(Vv54) + Yv22*complexconjugate(Vv55) + Yv32*complexconjugate(Vv56))*complexconjugate(Vv62) + (Yv13*complexconjugate(Vv54) + Yv23*complexconjugate(Vv55) + Yv33*complexconjugate(Vv56))*complexconjugate(Vv63) + complexconjugate(Vv51)*(Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66)) + complexconjugate(Vv52)*(Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66)) + complexconjugate(Vv53)*(Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_294 = Coupling(name = 'GC_294',
	 value = '(1*complex(0,1)*(Vv61*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + Vv51*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + Vv62*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + Vv52*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + Vv63*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33)) + Vv53*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_295 = Coupling(name = 'GC_295',
	 value = '(1*complex(0,1)*(2*complexconjugate(Vv61)*(Yv11*complexconjugate(Vv64) + Yv21*complexconjugate(Vv65) + Yv31*complexconjugate(Vv66)) + 2*complexconjugate(Vv62)*(Yv12*complexconjugate(Vv64) + Yv22*complexconjugate(Vv65) + Yv32*complexconjugate(Vv66)) + 2*complexconjugate(Vv63)*(Yv13*complexconjugate(Vv64) + Yv23*complexconjugate(Vv65) + Yv33*complexconjugate(Vv66))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_296 = Coupling(name = 'GC_296',
	 value = '(1*complex(0,1)*(2*Vv61*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + 2*Vv62*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + 2*Vv63*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33))))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_297 = Coupling(name = 'GC_297',
	 value = '-1*complex(0,1)*(complexconjugate(Vv11)*(Ye11*complexconjugate(ZER11) + Ye21*complexconjugate(ZER12) + Ye31*complexconjugate(ZER13)) + complexconjugate(Vv12)*(Ye12*complexconjugate(ZER11) + Ye22*complexconjugate(ZER12) + Ye32*complexconjugate(ZER13)) + complexconjugate(Vv13)*(Ye13*complexconjugate(ZER11) + Ye23*complexconjugate(ZER12) + Ye33*complexconjugate(ZER13)))', 
	 order = {'QED':1} ) 
 
GC_298 = Coupling(name = 'GC_298',
	 value = '-1*complex(0,1)*(ZEL11*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + ZEL12*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + ZEL13*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_299 = Coupling(name = 'GC_299',
	 value = '-1*complex(0,1)*(complexconjugate(Vv21)*(Ye11*complexconjugate(ZER11) + Ye21*complexconjugate(ZER12) + Ye31*complexconjugate(ZER13)) + complexconjugate(Vv22)*(Ye12*complexconjugate(ZER11) + Ye22*complexconjugate(ZER12) + Ye32*complexconjugate(ZER13)) + complexconjugate(Vv23)*(Ye13*complexconjugate(ZER11) + Ye23*complexconjugate(ZER12) + Ye33*complexconjugate(ZER13)))', 
	 order = {'QED':1} ) 
 
GC_300 = Coupling(name = 'GC_300',
	 value = '-1*complex(0,1)*(ZEL11*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + ZEL12*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + ZEL13*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_301 = Coupling(name = 'GC_301',
	 value = '-1*complex(0,1)*(complexconjugate(Vv31)*(Ye11*complexconjugate(ZER11) + Ye21*complexconjugate(ZER12) + Ye31*complexconjugate(ZER13)) + complexconjugate(Vv32)*(Ye12*complexconjugate(ZER11) + Ye22*complexconjugate(ZER12) + Ye32*complexconjugate(ZER13)) + complexconjugate(Vv33)*(Ye13*complexconjugate(ZER11) + Ye23*complexconjugate(ZER12) + Ye33*complexconjugate(ZER13)))', 
	 order = {'QED':1} ) 
 
GC_302 = Coupling(name = 'GC_302',
	 value = '-1*complex(0,1)*(ZEL11*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + ZEL12*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + ZEL13*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_303 = Coupling(name = 'GC_303',
	 value = '-1*complex(0,1)*(complexconjugate(Vv41)*(Ye11*complexconjugate(ZER11) + Ye21*complexconjugate(ZER12) + Ye31*complexconjugate(ZER13)) + complexconjugate(Vv42)*(Ye12*complexconjugate(ZER11) + Ye22*complexconjugate(ZER12) + Ye32*complexconjugate(ZER13)) + complexconjugate(Vv43)*(Ye13*complexconjugate(ZER11) + Ye23*complexconjugate(ZER12) + Ye33*complexconjugate(ZER13)))', 
	 order = {'QED':1} ) 
 
GC_304 = Coupling(name = 'GC_304',
	 value = '-1*complex(0,1)*(ZEL11*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + ZEL12*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + ZEL13*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_305 = Coupling(name = 'GC_305',
	 value = '-1*complex(0,1)*(complexconjugate(Vv51)*(Ye11*complexconjugate(ZER11) + Ye21*complexconjugate(ZER12) + Ye31*complexconjugate(ZER13)) + complexconjugate(Vv52)*(Ye12*complexconjugate(ZER11) + Ye22*complexconjugate(ZER12) + Ye32*complexconjugate(ZER13)) + complexconjugate(Vv53)*(Ye13*complexconjugate(ZER11) + Ye23*complexconjugate(ZER12) + Ye33*complexconjugate(ZER13)))', 
	 order = {'QED':1} ) 
 
GC_306 = Coupling(name = 'GC_306',
	 value = '-1*complex(0,1)*(ZEL11*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + ZEL12*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + ZEL13*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_307 = Coupling(name = 'GC_307',
	 value = '-1*complex(0,1)*(complexconjugate(Vv61)*(Ye11*complexconjugate(ZER11) + Ye21*complexconjugate(ZER12) + Ye31*complexconjugate(ZER13)) + complexconjugate(Vv62)*(Ye12*complexconjugate(ZER11) + Ye22*complexconjugate(ZER12) + Ye32*complexconjugate(ZER13)) + complexconjugate(Vv63)*(Ye13*complexconjugate(ZER11) + Ye23*complexconjugate(ZER12) + Ye33*complexconjugate(ZER13)))', 
	 order = {'QED':1} ) 
 
GC_308 = Coupling(name = 'GC_308',
	 value = '-1*complex(0,1)*(ZEL11*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + ZEL12*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + ZEL13*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_309 = Coupling(name = 'GC_309',
	 value = '-1*complex(0,1)*(complexconjugate(Vv11)*(Ye11*complexconjugate(ZER21) + Ye21*complexconjugate(ZER22) + Ye31*complexconjugate(ZER23)) + complexconjugate(Vv12)*(Ye12*complexconjugate(ZER21) + Ye22*complexconjugate(ZER22) + Ye32*complexconjugate(ZER23)) + complexconjugate(Vv13)*(Ye13*complexconjugate(ZER21) + Ye23*complexconjugate(ZER22) + Ye33*complexconjugate(ZER23)))', 
	 order = {'QED':1} ) 
 
GC_310 = Coupling(name = 'GC_310',
	 value = '-1*complex(0,1)*(ZEL21*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + ZEL22*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + ZEL23*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_311 = Coupling(name = 'GC_311',
	 value = '-1*complex(0,1)*(complexconjugate(Vv21)*(Ye11*complexconjugate(ZER21) + Ye21*complexconjugate(ZER22) + Ye31*complexconjugate(ZER23)) + complexconjugate(Vv22)*(Ye12*complexconjugate(ZER21) + Ye22*complexconjugate(ZER22) + Ye32*complexconjugate(ZER23)) + complexconjugate(Vv23)*(Ye13*complexconjugate(ZER21) + Ye23*complexconjugate(ZER22) + Ye33*complexconjugate(ZER23)))', 
	 order = {'QED':1} ) 
 
GC_312 = Coupling(name = 'GC_312',
	 value = '-1*complex(0,1)*(ZEL21*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + ZEL22*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + ZEL23*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_313 = Coupling(name = 'GC_313',
	 value = '-1*complex(0,1)*(complexconjugate(Vv31)*(Ye11*complexconjugate(ZER21) + Ye21*complexconjugate(ZER22) + Ye31*complexconjugate(ZER23)) + complexconjugate(Vv32)*(Ye12*complexconjugate(ZER21) + Ye22*complexconjugate(ZER22) + Ye32*complexconjugate(ZER23)) + complexconjugate(Vv33)*(Ye13*complexconjugate(ZER21) + Ye23*complexconjugate(ZER22) + Ye33*complexconjugate(ZER23)))', 
	 order = {'QED':1} ) 
 
GC_314 = Coupling(name = 'GC_314',
	 value = '-1*complex(0,1)*(ZEL21*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + ZEL22*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + ZEL23*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_315 = Coupling(name = 'GC_315',
	 value = '-1*complex(0,1)*(complexconjugate(Vv41)*(Ye11*complexconjugate(ZER21) + Ye21*complexconjugate(ZER22) + Ye31*complexconjugate(ZER23)) + complexconjugate(Vv42)*(Ye12*complexconjugate(ZER21) + Ye22*complexconjugate(ZER22) + Ye32*complexconjugate(ZER23)) + complexconjugate(Vv43)*(Ye13*complexconjugate(ZER21) + Ye23*complexconjugate(ZER22) + Ye33*complexconjugate(ZER23)))', 
	 order = {'QED':1} ) 
 
GC_316 = Coupling(name = 'GC_316',
	 value = '-1*complex(0,1)*(ZEL21*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + ZEL22*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + ZEL23*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_317 = Coupling(name = 'GC_317',
	 value = '-1*complex(0,1)*(complexconjugate(Vv51)*(Ye11*complexconjugate(ZER21) + Ye21*complexconjugate(ZER22) + Ye31*complexconjugate(ZER23)) + complexconjugate(Vv52)*(Ye12*complexconjugate(ZER21) + Ye22*complexconjugate(ZER22) + Ye32*complexconjugate(ZER23)) + complexconjugate(Vv53)*(Ye13*complexconjugate(ZER21) + Ye23*complexconjugate(ZER22) + Ye33*complexconjugate(ZER23)))', 
	 order = {'QED':1} ) 
 
GC_318 = Coupling(name = 'GC_318',
	 value = '-1*complex(0,1)*(ZEL21*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + ZEL22*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + ZEL23*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_319 = Coupling(name = 'GC_319',
	 value = '-1*complex(0,1)*(complexconjugate(Vv61)*(Ye11*complexconjugate(ZER21) + Ye21*complexconjugate(ZER22) + Ye31*complexconjugate(ZER23)) + complexconjugate(Vv62)*(Ye12*complexconjugate(ZER21) + Ye22*complexconjugate(ZER22) + Ye32*complexconjugate(ZER23)) + complexconjugate(Vv63)*(Ye13*complexconjugate(ZER21) + Ye23*complexconjugate(ZER22) + Ye33*complexconjugate(ZER23)))', 
	 order = {'QED':1} ) 
 
GC_320 = Coupling(name = 'GC_320',
	 value = '-1*complex(0,1)*(ZEL21*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + ZEL22*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + ZEL23*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_321 = Coupling(name = 'GC_321',
	 value = '-1*complex(0,1)*(complexconjugate(Vv11)*(Ye11*complexconjugate(ZER31) + Ye21*complexconjugate(ZER32) + Ye31*complexconjugate(ZER33)) + complexconjugate(Vv12)*(Ye12*complexconjugate(ZER31) + Ye22*complexconjugate(ZER32) + Ye32*complexconjugate(ZER33)) + complexconjugate(Vv13)*(Ye13*complexconjugate(ZER31) + Ye23*complexconjugate(ZER32) + Ye33*complexconjugate(ZER33)))', 
	 order = {'QED':1} ) 
 
GC_322 = Coupling(name = 'GC_322',
	 value = '-1*complex(0,1)*(ZEL31*(Vv14*complexconjugate(Yv11) + Vv15*complexconjugate(Yv21) + Vv16*complexconjugate(Yv31)) + ZEL32*(Vv14*complexconjugate(Yv12) + Vv15*complexconjugate(Yv22) + Vv16*complexconjugate(Yv32)) + ZEL33*(Vv14*complexconjugate(Yv13) + Vv15*complexconjugate(Yv23) + Vv16*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_323 = Coupling(name = 'GC_323',
	 value = '-1*complex(0,1)*(complexconjugate(Vv21)*(Ye11*complexconjugate(ZER31) + Ye21*complexconjugate(ZER32) + Ye31*complexconjugate(ZER33)) + complexconjugate(Vv22)*(Ye12*complexconjugate(ZER31) + Ye22*complexconjugate(ZER32) + Ye32*complexconjugate(ZER33)) + complexconjugate(Vv23)*(Ye13*complexconjugate(ZER31) + Ye23*complexconjugate(ZER32) + Ye33*complexconjugate(ZER33)))', 
	 order = {'QED':1} ) 
 
GC_324 = Coupling(name = 'GC_324',
	 value = '-1*complex(0,1)*(ZEL31*(Vv24*complexconjugate(Yv11) + Vv25*complexconjugate(Yv21) + Vv26*complexconjugate(Yv31)) + ZEL32*(Vv24*complexconjugate(Yv12) + Vv25*complexconjugate(Yv22) + Vv26*complexconjugate(Yv32)) + ZEL33*(Vv24*complexconjugate(Yv13) + Vv25*complexconjugate(Yv23) + Vv26*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_325 = Coupling(name = 'GC_325',
	 value = '-1*complex(0,1)*(complexconjugate(Vv31)*(Ye11*complexconjugate(ZER31) + Ye21*complexconjugate(ZER32) + Ye31*complexconjugate(ZER33)) + complexconjugate(Vv32)*(Ye12*complexconjugate(ZER31) + Ye22*complexconjugate(ZER32) + Ye32*complexconjugate(ZER33)) + complexconjugate(Vv33)*(Ye13*complexconjugate(ZER31) + Ye23*complexconjugate(ZER32) + Ye33*complexconjugate(ZER33)))', 
	 order = {'QED':1} ) 
 
GC_326 = Coupling(name = 'GC_326',
	 value = '-1*complex(0,1)*(ZEL31*(Vv34*complexconjugate(Yv11) + Vv35*complexconjugate(Yv21) + Vv36*complexconjugate(Yv31)) + ZEL32*(Vv34*complexconjugate(Yv12) + Vv35*complexconjugate(Yv22) + Vv36*complexconjugate(Yv32)) + ZEL33*(Vv34*complexconjugate(Yv13) + Vv35*complexconjugate(Yv23) + Vv36*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_327 = Coupling(name = 'GC_327',
	 value = '-1*complex(0,1)*(complexconjugate(Vv41)*(Ye11*complexconjugate(ZER31) + Ye21*complexconjugate(ZER32) + Ye31*complexconjugate(ZER33)) + complexconjugate(Vv42)*(Ye12*complexconjugate(ZER31) + Ye22*complexconjugate(ZER32) + Ye32*complexconjugate(ZER33)) + complexconjugate(Vv43)*(Ye13*complexconjugate(ZER31) + Ye23*complexconjugate(ZER32) + Ye33*complexconjugate(ZER33)))', 
	 order = {'QED':1} ) 
 
GC_328 = Coupling(name = 'GC_328',
	 value = '-1*complex(0,1)*(ZEL31*(Vv44*complexconjugate(Yv11) + Vv45*complexconjugate(Yv21) + Vv46*complexconjugate(Yv31)) + ZEL32*(Vv44*complexconjugate(Yv12) + Vv45*complexconjugate(Yv22) + Vv46*complexconjugate(Yv32)) + ZEL33*(Vv44*complexconjugate(Yv13) + Vv45*complexconjugate(Yv23) + Vv46*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_329 = Coupling(name = 'GC_329',
	 value = '-1*complex(0,1)*(complexconjugate(Vv51)*(Ye11*complexconjugate(ZER31) + Ye21*complexconjugate(ZER32) + Ye31*complexconjugate(ZER33)) + complexconjugate(Vv52)*(Ye12*complexconjugate(ZER31) + Ye22*complexconjugate(ZER32) + Ye32*complexconjugate(ZER33)) + complexconjugate(Vv53)*(Ye13*complexconjugate(ZER31) + Ye23*complexconjugate(ZER32) + Ye33*complexconjugate(ZER33)))', 
	 order = {'QED':1} ) 
 
GC_330 = Coupling(name = 'GC_330',
	 value = '-1*complex(0,1)*(ZEL31*(Vv54*complexconjugate(Yv11) + Vv55*complexconjugate(Yv21) + Vv56*complexconjugate(Yv31)) + ZEL32*(Vv54*complexconjugate(Yv12) + Vv55*complexconjugate(Yv22) + Vv56*complexconjugate(Yv32)) + ZEL33*(Vv54*complexconjugate(Yv13) + Vv55*complexconjugate(Yv23) + Vv56*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_331 = Coupling(name = 'GC_331',
	 value = '-1*complex(0,1)*(complexconjugate(Vv61)*(Ye11*complexconjugate(ZER31) + Ye21*complexconjugate(ZER32) + Ye31*complexconjugate(ZER33)) + complexconjugate(Vv62)*(Ye12*complexconjugate(ZER31) + Ye22*complexconjugate(ZER32) + Ye32*complexconjugate(ZER33)) + complexconjugate(Vv63)*(Ye13*complexconjugate(ZER31) + Ye23*complexconjugate(ZER32) + Ye33*complexconjugate(ZER33)))', 
	 order = {'QED':1} ) 
 
GC_332 = Coupling(name = 'GC_332',
	 value = '-1*complex(0,1)*(ZEL31*(Vv64*complexconjugate(Yv11) + Vv65*complexconjugate(Yv21) + Vv66*complexconjugate(Yv31)) + ZEL32*(Vv64*complexconjugate(Yv12) + Vv65*complexconjugate(Yv22) + Vv66*complexconjugate(Yv32)) + ZEL33*(Vv64*complexconjugate(Yv13) + Vv65*complexconjugate(Yv23) + Vv66*complexconjugate(Yv33)))', 
	 order = {'QED':1} ) 
 
GC_333 = Coupling(name = 'GC_333',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_334 = Coupling(name = 'GC_334',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_335 = Coupling(name = 'GC_335',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_336 = Coupling(name = 'GC_336',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_337 = Coupling(name = 'GC_337',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_338 = Coupling(name = 'GC_338',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_339 = Coupling(name = 'GC_339',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) - 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_340 = Coupling(name = 'GC_340',
	 value = '-1./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_341 = Coupling(name = 'GC_341',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) - 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_342 = Coupling(name = 'GC_342',
	 value = '-1./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_343 = Coupling(name = 'GC_343',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) - 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_344 = Coupling(name = 'GC_344',
	 value = '-1./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_345 = Coupling(name = 'GC_345',
	 value = '(1*complex(0,1)*g2*(ZUL11*complexconjugate(ZDL11) + ZUL12*complexconjugate(ZDL12) + ZUL13*complexconjugate(ZDL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_346 = Coupling(name = 'GC_346',
	 value = '(1*complex(0,1)*g2*(ZUL11*complexconjugate(ZDL21) + ZUL12*complexconjugate(ZDL22) + ZUL13*complexconjugate(ZDL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_347 = Coupling(name = 'GC_347',
	 value = '(1*complex(0,1)*g2*(ZUL11*complexconjugate(ZDL31) + ZUL12*complexconjugate(ZDL32) + ZUL13*complexconjugate(ZDL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_348 = Coupling(name = 'GC_348',
	 value = '(1*complex(0,1)*g2*(ZUL21*complexconjugate(ZDL11) + ZUL22*complexconjugate(ZDL12) + ZUL23*complexconjugate(ZDL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_349 = Coupling(name = 'GC_349',
	 value = '(1*complex(0,1)*g2*(ZUL21*complexconjugate(ZDL21) + ZUL22*complexconjugate(ZDL22) + ZUL23*complexconjugate(ZDL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_350 = Coupling(name = 'GC_350',
	 value = '(1*complex(0,1)*g2*(ZUL21*complexconjugate(ZDL31) + ZUL22*complexconjugate(ZDL32) + ZUL23*complexconjugate(ZDL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_351 = Coupling(name = 'GC_351',
	 value = '(1*complex(0,1)*g2*(ZUL31*complexconjugate(ZDL11) + ZUL32*complexconjugate(ZDL12) + ZUL33*complexconjugate(ZDL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_352 = Coupling(name = 'GC_352',
	 value = '(1*complex(0,1)*g2*(ZUL31*complexconjugate(ZDL21) + ZUL32*complexconjugate(ZDL22) + ZUL33*complexconjugate(ZDL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_353 = Coupling(name = 'GC_353',
	 value = '(1*complex(0,1)*g2*(ZUL31*complexconjugate(ZDL31) + ZUL32*complexconjugate(ZDL32) + ZUL33*complexconjugate(ZDL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_354 = Coupling(name = 'GC_354',
	 value = '-1./6.*complex(0,1)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_355 = Coupling(name = 'GC_355',
	 value = '1./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_356 = Coupling(name = 'GC_356',
	 value = '-1./6.*complex(0,1)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_357 = Coupling(name = 'GC_357',
	 value = '1./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_358 = Coupling(name = 'GC_358',
	 value = '-1./6.*complex(0,1)*(3*g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_359 = Coupling(name = 'GC_359',
	 value = '1./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_360 = Coupling(name = 'GC_360',
	 value = '(1*complex(0,1)*g2*(Vv11*complexconjugate(ZEL11) + Vv12*complexconjugate(ZEL12) + Vv13*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_361 = Coupling(name = 'GC_361',
	 value = '(1*complex(0,1)*g2*(Vv11*complexconjugate(ZEL21) + Vv12*complexconjugate(ZEL22) + Vv13*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_362 = Coupling(name = 'GC_362',
	 value = '(1*complex(0,1)*g2*(Vv11*complexconjugate(ZEL31) + Vv12*complexconjugate(ZEL32) + Vv13*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_363 = Coupling(name = 'GC_363',
	 value = '(1*complex(0,1)*g2*(Vv21*complexconjugate(ZEL11) + Vv22*complexconjugate(ZEL12) + Vv23*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_364 = Coupling(name = 'GC_364',
	 value = '(1*complex(0,1)*g2*(Vv21*complexconjugate(ZEL21) + Vv22*complexconjugate(ZEL22) + Vv23*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_365 = Coupling(name = 'GC_365',
	 value = '(1*complex(0,1)*g2*(Vv21*complexconjugate(ZEL31) + Vv22*complexconjugate(ZEL32) + Vv23*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_366 = Coupling(name = 'GC_366',
	 value = '(1*complex(0,1)*g2*(Vv31*complexconjugate(ZEL11) + Vv32*complexconjugate(ZEL12) + Vv33*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_367 = Coupling(name = 'GC_367',
	 value = '(1*complex(0,1)*g2*(Vv31*complexconjugate(ZEL21) + Vv32*complexconjugate(ZEL22) + Vv33*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_368 = Coupling(name = 'GC_368',
	 value = '(1*complex(0,1)*g2*(Vv31*complexconjugate(ZEL31) + Vv32*complexconjugate(ZEL32) + Vv33*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_369 = Coupling(name = 'GC_369',
	 value = '(1*complex(0,1)*g2*(Vv41*complexconjugate(ZEL11) + Vv42*complexconjugate(ZEL12) + Vv43*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_370 = Coupling(name = 'GC_370',
	 value = '(1*complex(0,1)*g2*(Vv41*complexconjugate(ZEL21) + Vv42*complexconjugate(ZEL22) + Vv43*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_371 = Coupling(name = 'GC_371',
	 value = '(1*complex(0,1)*g2*(Vv41*complexconjugate(ZEL31) + Vv42*complexconjugate(ZEL32) + Vv43*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_372 = Coupling(name = 'GC_372',
	 value = '(1*complex(0,1)*g2*(Vv51*complexconjugate(ZEL11) + Vv52*complexconjugate(ZEL12) + Vv53*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_373 = Coupling(name = 'GC_373',
	 value = '(1*complex(0,1)*g2*(Vv51*complexconjugate(ZEL21) + Vv52*complexconjugate(ZEL22) + Vv53*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_374 = Coupling(name = 'GC_374',
	 value = '(1*complex(0,1)*g2*(Vv51*complexconjugate(ZEL31) + Vv52*complexconjugate(ZEL32) + Vv53*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_375 = Coupling(name = 'GC_375',
	 value = '(1*complex(0,1)*g2*(Vv61*complexconjugate(ZEL11) + Vv62*complexconjugate(ZEL12) + Vv63*complexconjugate(ZEL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_376 = Coupling(name = 'GC_376',
	 value = '(1*complex(0,1)*g2*(Vv61*complexconjugate(ZEL21) + Vv62*complexconjugate(ZEL22) + Vv63*complexconjugate(ZEL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_377 = Coupling(name = 'GC_377',
	 value = '(1*complex(0,1)*g2*(Vv61*complexconjugate(ZEL31) + Vv62*complexconjugate(ZEL32) + Vv63*complexconjugate(ZEL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_378 = Coupling(name = 'GC_378',
	 value = '-1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_379 = Coupling(name = 'GC_379',
	 value = '-1*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_380 = Coupling(name = 'GC_380',
	 value = '-1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_381 = Coupling(name = 'GC_381',
	 value = '-1*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_382 = Coupling(name = 'GC_382',
	 value = '-1./2.*complex(0,1)*(g1*cmath.cos(TW) + g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_383 = Coupling(name = 'GC_383',
	 value = '-1*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_384 = Coupling(name = 'GC_384',
	 value = '-1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_385 = Coupling(name = 'GC_385',
	 value = '1*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_386 = Coupling(name = 'GC_386',
	 value = '-1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_387 = Coupling(name = 'GC_387',
	 value = '1*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_388 = Coupling(name = 'GC_388',
	 value = '-1./2.*complex(0,1)*(g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_389 = Coupling(name = 'GC_389',
	 value = '1*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_390 = Coupling(name = 'GC_390',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_391 = Coupling(name = 'GC_391',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_392 = Coupling(name = 'GC_392',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_393 = Coupling(name = 'GC_393',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_394 = Coupling(name = 'GC_394',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_395 = Coupling(name = 'GC_395',
	 value = '1*complex(0,1)*G', 
	 order = {'QCD':1} ) 
 
GC_396 = Coupling(name = 'GC_396',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) + 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_397 = Coupling(name = 'GC_397',
	 value = '2./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_398 = Coupling(name = 'GC_398',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) + 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_399 = Coupling(name = 'GC_399',
	 value = '2./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_400 = Coupling(name = 'GC_400',
	 value = '1./6.*complex(0,1)*(g1*cmath.cos(TW) + 3*g2*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_401 = Coupling(name = 'GC_401',
	 value = '2./3.*complex(0,1)*g1*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_402 = Coupling(name = 'GC_402',
	 value = '1./6.*complex(0,1)*(3*g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_403 = Coupling(name = 'GC_403',
	 value = '-2./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_404 = Coupling(name = 'GC_404',
	 value = '1./6.*complex(0,1)*(3*g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_405 = Coupling(name = 'GC_405',
	 value = '-2./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_406 = Coupling(name = 'GC_406',
	 value = '1./6.*complex(0,1)*(3*g2*cmath.cos(TW) - g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_407 = Coupling(name = 'GC_407',
	 value = '-2./3.*complex(0,1)*g1*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_408 = Coupling(name = 'GC_408',
	 value = '(1*complex(0,1)*g2*(ZDL11*complexconjugate(ZUL11) + ZDL12*complexconjugate(ZUL12) + ZDL13*complexconjugate(ZUL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_409 = Coupling(name = 'GC_409',
	 value = '(1*complex(0,1)*g2*(ZDL11*complexconjugate(ZUL21) + ZDL12*complexconjugate(ZUL22) + ZDL13*complexconjugate(ZUL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_410 = Coupling(name = 'GC_410',
	 value = '(1*complex(0,1)*g2*(ZDL11*complexconjugate(ZUL31) + ZDL12*complexconjugate(ZUL32) + ZDL13*complexconjugate(ZUL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_411 = Coupling(name = 'GC_411',
	 value = '(1*complex(0,1)*g2*(ZDL21*complexconjugate(ZUL11) + ZDL22*complexconjugate(ZUL12) + ZDL23*complexconjugate(ZUL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_412 = Coupling(name = 'GC_412',
	 value = '(1*complex(0,1)*g2*(ZDL21*complexconjugate(ZUL21) + ZDL22*complexconjugate(ZUL22) + ZDL23*complexconjugate(ZUL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_413 = Coupling(name = 'GC_413',
	 value = '(1*complex(0,1)*g2*(ZDL21*complexconjugate(ZUL31) + ZDL22*complexconjugate(ZUL32) + ZDL23*complexconjugate(ZUL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_414 = Coupling(name = 'GC_414',
	 value = '(1*complex(0,1)*g2*(ZDL31*complexconjugate(ZUL11) + ZDL32*complexconjugate(ZUL12) + ZDL33*complexconjugate(ZUL13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_415 = Coupling(name = 'GC_415',
	 value = '(1*complex(0,1)*g2*(ZDL31*complexconjugate(ZUL21) + ZDL32*complexconjugate(ZUL22) + ZDL33*complexconjugate(ZUL23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_416 = Coupling(name = 'GC_416',
	 value = '(1*complex(0,1)*g2*(ZDL31*complexconjugate(ZUL31) + ZDL32*complexconjugate(ZUL32) + ZDL33*complexconjugate(ZUL33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_417 = Coupling(name = 'GC_417',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv11) + Vv12*complexconjugate(Vv12) + Vv13*complexconjugate(Vv13))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_418 = Coupling(name = 'GC_418',
	 value = '-1./2.*complex(0,1)*(Vv11*complexconjugate(Vv11) + Vv12*complexconjugate(Vv12) + Vv13*complexconjugate(Vv13))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_419 = Coupling(name = 'GC_419',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv21) + Vv12*complexconjugate(Vv22) + Vv13*complexconjugate(Vv23))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_420 = Coupling(name = 'GC_420',
	 value = '-1./2.*complex(0,1)*(Vv21*complexconjugate(Vv11) + Vv22*complexconjugate(Vv12) + Vv23*complexconjugate(Vv13))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_421 = Coupling(name = 'GC_421',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv31) + Vv12*complexconjugate(Vv32) + Vv13*complexconjugate(Vv33))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_422 = Coupling(name = 'GC_422',
	 value = '-1./2.*complex(0,1)*(Vv31*complexconjugate(Vv11) + Vv32*complexconjugate(Vv12) + Vv33*complexconjugate(Vv13))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_423 = Coupling(name = 'GC_423',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv41) + Vv12*complexconjugate(Vv42) + Vv13*complexconjugate(Vv43))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_424 = Coupling(name = 'GC_424',
	 value = '-1./2.*complex(0,1)*(Vv41*complexconjugate(Vv11) + Vv42*complexconjugate(Vv12) + Vv43*complexconjugate(Vv13))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_425 = Coupling(name = 'GC_425',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv51) + Vv12*complexconjugate(Vv52) + Vv13*complexconjugate(Vv53))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_426 = Coupling(name = 'GC_426',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv11) + Vv52*complexconjugate(Vv12) + Vv53*complexconjugate(Vv13))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_427 = Coupling(name = 'GC_427',
	 value = '1./2.*complex(0,1)*(Vv11*complexconjugate(Vv61) + Vv12*complexconjugate(Vv62) + Vv13*complexconjugate(Vv63))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_428 = Coupling(name = 'GC_428',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv11) + Vv62*complexconjugate(Vv12) + Vv63*complexconjugate(Vv13))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_429 = Coupling(name = 'GC_429',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv21) + Vv22*complexconjugate(Vv22) + Vv23*complexconjugate(Vv23))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_430 = Coupling(name = 'GC_430',
	 value = '-1./2.*complex(0,1)*(Vv21*complexconjugate(Vv21) + Vv22*complexconjugate(Vv22) + Vv23*complexconjugate(Vv23))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_431 = Coupling(name = 'GC_431',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv31) + Vv22*complexconjugate(Vv32) + Vv23*complexconjugate(Vv33))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_432 = Coupling(name = 'GC_432',
	 value = '-1./2.*complex(0,1)*(Vv31*complexconjugate(Vv21) + Vv32*complexconjugate(Vv22) + Vv33*complexconjugate(Vv23))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_433 = Coupling(name = 'GC_433',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv41) + Vv22*complexconjugate(Vv42) + Vv23*complexconjugate(Vv43))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_434 = Coupling(name = 'GC_434',
	 value = '-1./2.*complex(0,1)*(Vv41*complexconjugate(Vv21) + Vv42*complexconjugate(Vv22) + Vv43*complexconjugate(Vv23))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_435 = Coupling(name = 'GC_435',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv51) + Vv22*complexconjugate(Vv52) + Vv23*complexconjugate(Vv53))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_436 = Coupling(name = 'GC_436',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv21) + Vv52*complexconjugate(Vv22) + Vv53*complexconjugate(Vv23))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_437 = Coupling(name = 'GC_437',
	 value = '1./2.*complex(0,1)*(Vv21*complexconjugate(Vv61) + Vv22*complexconjugate(Vv62) + Vv23*complexconjugate(Vv63))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_438 = Coupling(name = 'GC_438',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv21) + Vv62*complexconjugate(Vv22) + Vv63*complexconjugate(Vv23))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_439 = Coupling(name = 'GC_439',
	 value = '1./2.*complex(0,1)*(Vv31*complexconjugate(Vv31) + Vv32*complexconjugate(Vv32) + Vv33*complexconjugate(Vv33))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_440 = Coupling(name = 'GC_440',
	 value = '-1./2.*complex(0,1)*(Vv31*complexconjugate(Vv31) + Vv32*complexconjugate(Vv32) + Vv33*complexconjugate(Vv33))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_441 = Coupling(name = 'GC_441',
	 value = '1./2.*complex(0,1)*(Vv31*complexconjugate(Vv41) + Vv32*complexconjugate(Vv42) + Vv33*complexconjugate(Vv43))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_442 = Coupling(name = 'GC_442',
	 value = '-1./2.*complex(0,1)*(Vv41*complexconjugate(Vv31) + Vv42*complexconjugate(Vv32) + Vv43*complexconjugate(Vv33))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_443 = Coupling(name = 'GC_443',
	 value = '1./2.*complex(0,1)*(Vv31*complexconjugate(Vv51) + Vv32*complexconjugate(Vv52) + Vv33*complexconjugate(Vv53))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_444 = Coupling(name = 'GC_444',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv31) + Vv52*complexconjugate(Vv32) + Vv53*complexconjugate(Vv33))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_445 = Coupling(name = 'GC_445',
	 value = '1./2.*complex(0,1)*(Vv31*complexconjugate(Vv61) + Vv32*complexconjugate(Vv62) + Vv33*complexconjugate(Vv63))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_446 = Coupling(name = 'GC_446',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv31) + Vv62*complexconjugate(Vv32) + Vv63*complexconjugate(Vv33))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_447 = Coupling(name = 'GC_447',
	 value = '1./2.*complex(0,1)*(Vv41*complexconjugate(Vv41) + Vv42*complexconjugate(Vv42) + Vv43*complexconjugate(Vv43))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_448 = Coupling(name = 'GC_448',
	 value = '-1./2.*complex(0,1)*(Vv41*complexconjugate(Vv41) + Vv42*complexconjugate(Vv42) + Vv43*complexconjugate(Vv43))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_449 = Coupling(name = 'GC_449',
	 value = '1./2.*complex(0,1)*(Vv41*complexconjugate(Vv51) + Vv42*complexconjugate(Vv52) + Vv43*complexconjugate(Vv53))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_450 = Coupling(name = 'GC_450',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv41) + Vv52*complexconjugate(Vv42) + Vv53*complexconjugate(Vv43))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_451 = Coupling(name = 'GC_451',
	 value = '1./2.*complex(0,1)*(Vv41*complexconjugate(Vv61) + Vv42*complexconjugate(Vv62) + Vv43*complexconjugate(Vv63))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_452 = Coupling(name = 'GC_452',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv41) + Vv62*complexconjugate(Vv42) + Vv63*complexconjugate(Vv43))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_453 = Coupling(name = 'GC_453',
	 value = '1./2.*complex(0,1)*(Vv51*complexconjugate(Vv51) + Vv52*complexconjugate(Vv52) + Vv53*complexconjugate(Vv53))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_454 = Coupling(name = 'GC_454',
	 value = '-1./2.*complex(0,1)*(Vv51*complexconjugate(Vv51) + Vv52*complexconjugate(Vv52) + Vv53*complexconjugate(Vv53))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_455 = Coupling(name = 'GC_455',
	 value = '1./2.*complex(0,1)*(Vv51*complexconjugate(Vv61) + Vv52*complexconjugate(Vv62) + Vv53*complexconjugate(Vv63))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_456 = Coupling(name = 'GC_456',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv51) + Vv62*complexconjugate(Vv52) + Vv63*complexconjugate(Vv53))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_457 = Coupling(name = 'GC_457',
	 value = '1./2.*complex(0,1)*(Vv61*complexconjugate(Vv61) + Vv62*complexconjugate(Vv62) + Vv63*complexconjugate(Vv63))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_458 = Coupling(name = 'GC_458',
	 value = '-1./2.*complex(0,1)*(Vv61*complexconjugate(Vv61) + Vv62*complexconjugate(Vv62) + Vv63*complexconjugate(Vv63))*(g2*cmath.cos(TW) + g1*cmath.sin(TW))', 
	 order = {'QED':1} ) 
 
GC_459 = Coupling(name = 'GC_459',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(Vv11) + ZEL12*complexconjugate(Vv12) + ZEL13*complexconjugate(Vv13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_460 = Coupling(name = 'GC_460',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(Vv21) + ZEL12*complexconjugate(Vv22) + ZEL13*complexconjugate(Vv23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_461 = Coupling(name = 'GC_461',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(Vv31) + ZEL12*complexconjugate(Vv32) + ZEL13*complexconjugate(Vv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_462 = Coupling(name = 'GC_462',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(Vv41) + ZEL12*complexconjugate(Vv42) + ZEL13*complexconjugate(Vv43)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_463 = Coupling(name = 'GC_463',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(Vv51) + ZEL12*complexconjugate(Vv52) + ZEL13*complexconjugate(Vv53)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_464 = Coupling(name = 'GC_464',
	 value = '(1*complex(0,1)*g2*(ZEL11*complexconjugate(Vv61) + ZEL12*complexconjugate(Vv62) + ZEL13*complexconjugate(Vv63)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_465 = Coupling(name = 'GC_465',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(Vv11) + ZEL22*complexconjugate(Vv12) + ZEL23*complexconjugate(Vv13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_466 = Coupling(name = 'GC_466',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(Vv21) + ZEL22*complexconjugate(Vv22) + ZEL23*complexconjugate(Vv23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_467 = Coupling(name = 'GC_467',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(Vv31) + ZEL22*complexconjugate(Vv32) + ZEL23*complexconjugate(Vv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_468 = Coupling(name = 'GC_468',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(Vv41) + ZEL22*complexconjugate(Vv42) + ZEL23*complexconjugate(Vv43)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_469 = Coupling(name = 'GC_469',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(Vv51) + ZEL22*complexconjugate(Vv52) + ZEL23*complexconjugate(Vv53)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_470 = Coupling(name = 'GC_470',
	 value = '(1*complex(0,1)*g2*(ZEL21*complexconjugate(Vv61) + ZEL22*complexconjugate(Vv62) + ZEL23*complexconjugate(Vv63)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_471 = Coupling(name = 'GC_471',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(Vv11) + ZEL32*complexconjugate(Vv12) + ZEL33*complexconjugate(Vv13)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_472 = Coupling(name = 'GC_472',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(Vv21) + ZEL32*complexconjugate(Vv22) + ZEL33*complexconjugate(Vv23)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_473 = Coupling(name = 'GC_473',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(Vv31) + ZEL32*complexconjugate(Vv32) + ZEL33*complexconjugate(Vv33)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_474 = Coupling(name = 'GC_474',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(Vv41) + ZEL32*complexconjugate(Vv42) + ZEL33*complexconjugate(Vv43)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_475 = Coupling(name = 'GC_475',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(Vv51) + ZEL32*complexconjugate(Vv52) + ZEL33*complexconjugate(Vv53)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_476 = Coupling(name = 'GC_476',
	 value = '(1*complex(0,1)*g2*(ZEL31*complexconjugate(Vv61) + ZEL32*complexconjugate(Vv62) + ZEL33*complexconjugate(Vv63)))/cmath.sqrt(2)', 
	 order = {'QED':1} ) 
 
GC_477 = Coupling(name = 'GC_477',
	 value = 'G', 
	 order = {'QCD':1} ) 
 
GC_478 = Coupling(name = 'GC_478',
	 value = '1*complex(0,1)*g2*cmath.sin(TW)', 
	 order = {'QED':1} ) 
 
GC_479 = Coupling(name = 'GC_479',
	 value = '-1*complex(0,1)*g2*cmath.cos(TW)', 
	 order = {'QED':1} ) 
 
GC_480 = Coupling(name = 'GC_480',
	 value = '-1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_481 = Coupling(name = 'GC_481',
	 value = '-1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_482 = Coupling(name = 'GC_482',
	 value = '1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_483 = Coupling(name = 'GC_483',
	 value = '-1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_484 = Coupling(name = 'GC_484',
	 value = '1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_485 = Coupling(name = 'GC_485',
	 value = '1*complex(0,1)*G**2', 
	 order = {'QCD':2} ) 
 
GC_486 = Coupling(name = 'GC_486',
	 value = '1*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_487 = Coupling(name = 'GC_487',
	 value = '1*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_488 = Coupling(name = 'GC_488',
	 value = '-2*complex(0,1)*g2**2*cmath.sin(TW)**2', 
	 order = {'QED':2} ) 
 
GC_489 = Coupling(name = 'GC_489',
	 value = '1*complex(0,1)*g2**2*cmath.cos(TW)*cmath.sin(TW)', 
	 order = {'QED':2} ) 
 
GC_490 = Coupling(name = 'GC_490',
	 value = '-1*complex(0,1)*g2**2*cmath.sin(2*TW)', 
	 order = {'QED':2} ) 
 
GC_491 = Coupling(name = 'GC_491',
	 value = '1*complex(0,1)*g2**2*cmath.cos(TW)*cmath.sin(TW)', 
	 order = {'QED':2} ) 
 
GC_492 = Coupling(name = 'GC_492',
	 value = '2*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_493 = Coupling(name = 'GC_493',
	 value = '-1*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_494 = Coupling(name = 'GC_494',
	 value = '-1*complex(0,1)*g2**2', 
	 order = {'QED':2} ) 
 
GC_495 = Coupling(name = 'GC_495',
	 value = '-2*complex(0,1)*g2**2*cmath.cos(TW)**2', 
	 order = {'QED':2} ) 
 
GC_496 = Coupling(name = 'GC_496',
	 value = '1*complex(0,1)*g2**2*cmath.cos(TW)**2', 
	 order = {'QED':2} ) 
 
GC_497 = Coupling(name = 'GC_497',
	 value = '1*complex(0,1)*g2**2*cmath.cos(TW)**2', 
	 order = {'QED':2} ) 
 
GC_498=Coupling(name='GC_498',
	 value='-(HPP1*complex(0,1))', 
	 order={'HIW':1})

GC_499=Coupling(name='GC_499',
	 value='-(HGG1*complex(0,1))', 
	 order={'HIG':1})

