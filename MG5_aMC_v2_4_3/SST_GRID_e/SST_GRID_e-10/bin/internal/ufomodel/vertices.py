# ------------------------------------------------------------------------------  
# This model file was automatically created by SARAH version4.12.2 
# SARAH References: arXiv:0806.0538, 0909.2863, 1002.0840, 1207.0906, 1309.7223   
# (c) Florian Staub, 2013  
# -------------------------------------------------------------------------------  
# File created at 14:50 on 5.12.2017   
# ----------------------------------------------------------------------  
 
 
from object_library import all_vertices,Vertex 
import particles as P 
import couplings as C 
import lorentz as L 
 
 
V_1 = Vertex(name = 'V_1', 
	 particles = [P.Ah, P.Ah, P.h], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_1}) 
 
 
V_2 = Vertex(name = 'V_2', 
	 particles = [P.h, P.h, P.h], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_2}) 
 
 
V_3 = Vertex(name = 'V_3', 
	 particles = [P.h, P.Hp, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.SSS1], 
	 couplings = {(0,0):C.GC_3}) 
 
 
V_4 = Vertex(name = 'V_4', 
	 particles = [P.Ah, P.Ah, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_4}) 
 
 
V_5 = Vertex(name = 'V_5', 
	 particles = [P.Ah, P.Ah, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_5}) 
 
 
V_6 = Vertex(name = 'V_6', 
	 particles = [P.Ah, P.Hp, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_6}) 
 
 
V_7 = Vertex(name = 'V_7', 
	 particles = [P.Ah, P.Hp, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_7}) 
 
 
V_8 = Vertex(name = 'V_8', 
	 particles = [P.Ah, P.Hpc, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_8}) 
 
 
V_9 = Vertex(name = 'V_9', 
	 particles = [P.Ah, P.Hpc, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_9}) 
 
 
V_10 = Vertex(name = 'V_10', 
	 particles = [P.h, P.h, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_10}) 
 
 
V_11 = Vertex(name = 'V_11', 
	 particles = [P.h, P.h, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_11}) 
 
 
V_12 = Vertex(name = 'V_12', 
	 particles = [P.h, P.Hp, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_12}) 
 
 
V_13 = Vertex(name = 'V_13', 
	 particles = [P.h, P.Hp, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_13}) 
 
 
V_14 = Vertex(name = 'V_14', 
	 particles = [P.h, P.Hpc, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_14}) 
 
 
V_15 = Vertex(name = 'V_15', 
	 particles = [P.h, P.Hpc, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_15}) 
 
 
V_16 = Vertex(name = 'V_16', 
	 particles = [P.Hp, P.Hpc, P.A, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_16}) 
 
 
V_17 = Vertex(name = 'V_17', 
	 particles = [P.Hp, P.Hpc, P.A, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_17}) 
 
 
V_18 = Vertex(name = 'V_18', 
	 particles = [P.Hp, P.Hpc, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_18}) 
 
 
V_19 = Vertex(name = 'V_19', 
	 particles = [P.Hp, P.Hpc, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSVV1], 
	 couplings = {(0,0):C.GC_19}) 
 
 
V_20 = Vertex(name = 'V_20', 
	 particles = [P.Ah, P.h, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_20}) 
 
 
V_21 = Vertex(name = 'V_21', 
	 particles = [P.Ah, P.Hp, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_21}) 
 
 
V_22 = Vertex(name = 'V_22', 
	 particles = [P.Ah, P.Hpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_22}) 
 
 
V_23 = Vertex(name = 'V_23', 
	 particles = [P.h, P.Hp, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_23}) 
 
 
V_24 = Vertex(name = 'V_24', 
	 particles = [P.h, P.Hpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_24}) 
 
 
V_25 = Vertex(name = 'V_25', 
	 particles = [P.Hp, P.Hpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_25}) 
 
 
V_26 = Vertex(name = 'V_26', 
	 particles = [P.Hp, P.Hpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SSV1], 
	 couplings = {(0,0):C.GC_26}) 
 
 
V_27 = Vertex(name = 'V_27', 
	 particles = [P.h, P.Wpc, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_27}) 
 
 
V_28 = Vertex(name = 'V_28', 
	 particles = [P.h, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_28}) 
 
 
V_29 = Vertex(name = 'V_29', 
	 particles = [P.Hp, P.Wpc, P.A], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_29}) 
 
 
V_30 = Vertex(name = 'V_30', 
	 particles = [P.Hp, P.Wpc, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_30}) 
 
 
V_31 = Vertex(name = 'V_31', 
	 particles = [P.Hpc, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_31}) 
 
 
V_32 = Vertex(name = 'V_32', 
	 particles = [P.Hpc, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.SVV1], 
	 couplings = {(0,0):C.GC_32}) 
 
 
V_33 = Vertex(name = 'V_33', 
	 particles = [P.d1bar, P.d1, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_33,(0,1):C.GC_34}) 
 
 
V_34 = Vertex(name = 'V_34', 
	 particles = [P.d1bar, P.d2, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_35,(0,1):C.GC_36}) 
 
 
V_35 = Vertex(name = 'V_35', 
	 particles = [P.d1bar, P.d3, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_37,(0,1):C.GC_38}) 
 
 
V_36 = Vertex(name = 'V_36', 
	 particles = [P.d2bar, P.d1, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_39,(0,1):C.GC_40}) 
 
 
V_37 = Vertex(name = 'V_37', 
	 particles = [P.d2bar, P.d2, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_41,(0,1):C.GC_42}) 
 
 
V_38 = Vertex(name = 'V_38', 
	 particles = [P.d2bar, P.d3, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_43,(0,1):C.GC_44}) 
 
 
V_39 = Vertex(name = 'V_39', 
	 particles = [P.d3bar, P.d1, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_45,(0,1):C.GC_46}) 
 
 
V_40 = Vertex(name = 'V_40', 
	 particles = [P.d3bar, P.d2, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_47,(0,1):C.GC_48}) 
 
 
V_41 = Vertex(name = 'V_41', 
	 particles = [P.d3bar, P.d3, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_49,(0,1):C.GC_50}) 
 
 
V_42 = Vertex(name = 'V_42', 
	 particles = [P.e1bar, P.e1, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_51,(0,1):C.GC_52}) 
 
 
V_43 = Vertex(name = 'V_43', 
	 particles = [P.e1bar, P.e2, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_53,(0,1):C.GC_54}) 
 
 
V_44 = Vertex(name = 'V_44', 
	 particles = [P.e1bar, P.e3, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_55,(0,1):C.GC_56}) 
 
 
V_45 = Vertex(name = 'V_45', 
	 particles = [P.e2bar, P.e1, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_57,(0,1):C.GC_58}) 
 
 
V_46 = Vertex(name = 'V_46', 
	 particles = [P.e2bar, P.e2, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_59,(0,1):C.GC_60}) 
 
 
V_47 = Vertex(name = 'V_47', 
	 particles = [P.e2bar, P.e3, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_61,(0,1):C.GC_62}) 
 
 
V_48 = Vertex(name = 'V_48', 
	 particles = [P.e3bar, P.e1, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_63,(0,1):C.GC_64}) 
 
 
V_49 = Vertex(name = 'V_49', 
	 particles = [P.e3bar, P.e2, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_65,(0,1):C.GC_66}) 
 
 
V_50 = Vertex(name = 'V_50', 
	 particles = [P.e3bar, P.e3, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_67,(0,1):C.GC_68}) 
 
 
V_51 = Vertex(name = 'V_51', 
	 particles = [P.u1bar, P.u1, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_69,(0,1):C.GC_70}) 
 
 
V_52 = Vertex(name = 'V_52', 
	 particles = [P.u1bar, P.u2, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_71,(0,1):C.GC_72}) 
 
 
V_53 = Vertex(name = 'V_53', 
	 particles = [P.u1bar, P.u3, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_73,(0,1):C.GC_74}) 
 
 
V_54 = Vertex(name = 'V_54', 
	 particles = [P.u2bar, P.u1, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_75,(0,1):C.GC_76}) 
 
 
V_55 = Vertex(name = 'V_55', 
	 particles = [P.u2bar, P.u2, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_77,(0,1):C.GC_78}) 
 
 
V_56 = Vertex(name = 'V_56', 
	 particles = [P.u2bar, P.u3, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_79,(0,1):C.GC_80}) 
 
 
V_57 = Vertex(name = 'V_57', 
	 particles = [P.u3bar, P.u1, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_81,(0,1):C.GC_82}) 
 
 
V_58 = Vertex(name = 'V_58', 
	 particles = [P.u3bar, P.u2, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_83,(0,1):C.GC_84}) 
 
 
V_59 = Vertex(name = 'V_59', 
	 particles = [P.u3bar, P.u3, P.Ah], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_85,(0,1):C.GC_86}) 
 
 
V_60 = Vertex(name = 'V_60', 
	 particles = [P.nu1, P.nu1, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_87,(0,1):C.GC_88}) 
 
 
V_61 = Vertex(name = 'V_61', 
	 particles = [P.nu1, P.nu2, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_89,(0,1):C.GC_90}) 
 
 
V_62 = Vertex(name = 'V_62', 
	 particles = [P.nu1, P.nu3, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_91,(0,1):C.GC_92}) 
 
 
V_63 = Vertex(name = 'V_63', 
	 particles = [P.nu1, P.nu4, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_93,(0,1):C.GC_94}) 
 
 
V_64 = Vertex(name = 'V_64', 
	 particles = [P.nu1, P.nu5, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_95,(0,1):C.GC_96}) 
 
 
V_65 = Vertex(name = 'V_65', 
	 particles = [P.nu1, P.nu6, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_97,(0,1):C.GC_98}) 
 
 
V_66 = Vertex(name = 'V_66', 
	 particles = [P.nu2, P.nu2, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_99,(0,1):C.GC_100}) 
 
 
V_67 = Vertex(name = 'V_67', 
	 particles = [P.nu2, P.nu3, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_101,(0,1):C.GC_102}) 
 
 
V_68 = Vertex(name = 'V_68', 
	 particles = [P.nu2, P.nu4, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_103,(0,1):C.GC_104}) 
 
 
V_69 = Vertex(name = 'V_69', 
	 particles = [P.nu2, P.nu5, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_105,(0,1):C.GC_106}) 
 
 
V_70 = Vertex(name = 'V_70', 
	 particles = [P.nu2, P.nu6, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_107,(0,1):C.GC_108}) 
 
 
V_71 = Vertex(name = 'V_71', 
	 particles = [P.nu3, P.nu3, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_109,(0,1):C.GC_110}) 
 
 
V_72 = Vertex(name = 'V_72', 
	 particles = [P.nu3, P.nu4, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_111,(0,1):C.GC_112}) 
 
 
V_73 = Vertex(name = 'V_73', 
	 particles = [P.nu3, P.nu5, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_113,(0,1):C.GC_114}) 
 
 
V_74 = Vertex(name = 'V_74', 
	 particles = [P.nu3, P.nu6, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_115,(0,1):C.GC_116}) 
 
 
V_75 = Vertex(name = 'V_75', 
	 particles = [P.nu4, P.nu4, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_117,(0,1):C.GC_118}) 
 
 
V_76 = Vertex(name = 'V_76', 
	 particles = [P.nu4, P.nu5, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_119,(0,1):C.GC_120}) 
 
 
V_77 = Vertex(name = 'V_77', 
	 particles = [P.nu4, P.nu6, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_121,(0,1):C.GC_122}) 
 
 
V_78 = Vertex(name = 'V_78', 
	 particles = [P.nu5, P.nu5, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_123,(0,1):C.GC_124}) 
 
 
V_79 = Vertex(name = 'V_79', 
	 particles = [P.nu5, P.nu6, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_125,(0,1):C.GC_126}) 
 
 
V_80 = Vertex(name = 'V_80', 
	 particles = [P.nu6, P.nu6, P.Ah], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_127,(0,1):C.GC_128}) 
 
 
V_81 = Vertex(name = 'V_81', 
	 particles = [P.d1bar, P.d1, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_129,(0,1):C.GC_130}) 
 
 
V_82 = Vertex(name = 'V_82', 
	 particles = [P.d1bar, P.d2, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_131,(0,1):C.GC_132}) 
 
 
V_83 = Vertex(name = 'V_83', 
	 particles = [P.d1bar, P.d3, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_133,(0,1):C.GC_134}) 
 
 
V_84 = Vertex(name = 'V_84', 
	 particles = [P.d2bar, P.d1, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_135,(0,1):C.GC_136}) 
 
 
V_85 = Vertex(name = 'V_85', 
	 particles = [P.d2bar, P.d2, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_137,(0,1):C.GC_138}) 
 
 
V_86 = Vertex(name = 'V_86', 
	 particles = [P.d2bar, P.d3, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_139,(0,1):C.GC_140}) 
 
 
V_87 = Vertex(name = 'V_87', 
	 particles = [P.d3bar, P.d1, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_141,(0,1):C.GC_142}) 
 
 
V_88 = Vertex(name = 'V_88', 
	 particles = [P.d3bar, P.d2, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_143,(0,1):C.GC_144}) 
 
 
V_89 = Vertex(name = 'V_89', 
	 particles = [P.d3bar, P.d3, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_145,(0,1):C.GC_146}) 
 
 
V_90 = Vertex(name = 'V_90', 
	 particles = [P.u1bar, P.d1, P.Hp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_147,(0,1):C.GC_148}) 
 
 
V_91 = Vertex(name = 'V_91', 
	 particles = [P.u1bar, P.d2, P.Hp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_149,(0,1):C.GC_150}) 
 
 
V_92 = Vertex(name = 'V_92', 
	 particles = [P.u1bar, P.d3, P.Hp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_151,(0,1):C.GC_152}) 
 
 
V_93 = Vertex(name = 'V_93', 
	 particles = [P.u2bar, P.d1, P.Hp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_153,(0,1):C.GC_154}) 
 
 
V_94 = Vertex(name = 'V_94', 
	 particles = [P.u2bar, P.d2, P.Hp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_155,(0,1):C.GC_156}) 
 
 
V_95 = Vertex(name = 'V_95', 
	 particles = [P.u2bar, P.d3, P.Hp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_157,(0,1):C.GC_158}) 
 
 
V_96 = Vertex(name = 'V_96', 
	 particles = [P.u3bar, P.d1, P.Hp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_159,(0,1):C.GC_160}) 
 
 
V_97 = Vertex(name = 'V_97', 
	 particles = [P.u3bar, P.d2, P.Hp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_161,(0,1):C.GC_162}) 
 
 
V_98 = Vertex(name = 'V_98', 
	 particles = [P.u3bar, P.d3, P.Hp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_163,(0,1):C.GC_164}) 
 
 
V_99 = Vertex(name = 'V_99', 
	 particles = [P.nu1, P.e1, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_165,(0,1):C.GC_166}) 
 
 
V_100 = Vertex(name = 'V_100', 
	 particles = [P.nu1, P.e2, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_167,(0,1):C.GC_168}) 
 
 
V_101 = Vertex(name = 'V_101', 
	 particles = [P.nu1, P.e3, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_169,(0,1):C.GC_170}) 
 
 
V_102 = Vertex(name = 'V_102', 
	 particles = [P.nu2, P.e1, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_171,(0,1):C.GC_172}) 
 
 
V_103 = Vertex(name = 'V_103', 
	 particles = [P.nu2, P.e2, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_173,(0,1):C.GC_174}) 
 
 
V_104 = Vertex(name = 'V_104', 
	 particles = [P.nu2, P.e3, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_175,(0,1):C.GC_176}) 
 
 
V_105 = Vertex(name = 'V_105', 
	 particles = [P.nu3, P.e1, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_177,(0,1):C.GC_178}) 
 
 
V_106 = Vertex(name = 'V_106', 
	 particles = [P.nu3, P.e2, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_179,(0,1):C.GC_180}) 
 
 
V_107 = Vertex(name = 'V_107', 
	 particles = [P.nu3, P.e3, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_181,(0,1):C.GC_182}) 
 
 
V_108 = Vertex(name = 'V_108', 
	 particles = [P.nu4, P.e1, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_183,(0,1):C.GC_184}) 
 
 
V_109 = Vertex(name = 'V_109', 
	 particles = [P.nu4, P.e2, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_185,(0,1):C.GC_186}) 
 
 
V_110 = Vertex(name = 'V_110', 
	 particles = [P.nu4, P.e3, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_187,(0,1):C.GC_188}) 
 
 
V_111 = Vertex(name = 'V_111', 
	 particles = [P.nu5, P.e1, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_189,(0,1):C.GC_190}) 
 
 
V_112 = Vertex(name = 'V_112', 
	 particles = [P.nu5, P.e2, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_191,(0,1):C.GC_192}) 
 
 
V_113 = Vertex(name = 'V_113', 
	 particles = [P.nu5, P.e3, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_193,(0,1):C.GC_194}) 
 
 
V_114 = Vertex(name = 'V_114', 
	 particles = [P.nu6, P.e1, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_195,(0,1):C.GC_196}) 
 
 
V_115 = Vertex(name = 'V_115', 
	 particles = [P.nu6, P.e2, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_197,(0,1):C.GC_198}) 
 
 
V_116 = Vertex(name = 'V_116', 
	 particles = [P.nu6, P.e3, P.Hp], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_199,(0,1):C.GC_200}) 
 
 
V_117 = Vertex(name = 'V_117', 
	 particles = [P.e1bar, P.e1, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_201,(0,1):C.GC_202}) 
 
 
V_118 = Vertex(name = 'V_118', 
	 particles = [P.e1bar, P.e2, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_203,(0,1):C.GC_204}) 
 
 
V_119 = Vertex(name = 'V_119', 
	 particles = [P.e1bar, P.e3, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_205,(0,1):C.GC_206}) 
 
 
V_120 = Vertex(name = 'V_120', 
	 particles = [P.e2bar, P.e1, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_207,(0,1):C.GC_208}) 
 
 
V_121 = Vertex(name = 'V_121', 
	 particles = [P.e2bar, P.e2, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_209,(0,1):C.GC_210}) 
 
 
V_122 = Vertex(name = 'V_122', 
	 particles = [P.e2bar, P.e3, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_211,(0,1):C.GC_212}) 
 
 
V_123 = Vertex(name = 'V_123', 
	 particles = [P.e3bar, P.e1, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_213,(0,1):C.GC_214}) 
 
 
V_124 = Vertex(name = 'V_124', 
	 particles = [P.e3bar, P.e2, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_215,(0,1):C.GC_216}) 
 
 
V_125 = Vertex(name = 'V_125', 
	 particles = [P.e3bar, P.e3, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_217,(0,1):C.GC_218}) 
 
 
V_126 = Vertex(name = 'V_126', 
	 particles = [P.u1bar, P.u1, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_219,(0,1):C.GC_220}) 
 
 
V_127 = Vertex(name = 'V_127', 
	 particles = [P.u1bar, P.u2, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_221,(0,1):C.GC_222}) 
 
 
V_128 = Vertex(name = 'V_128', 
	 particles = [P.u1bar, P.u3, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_223,(0,1):C.GC_224}) 
 
 
V_129 = Vertex(name = 'V_129', 
	 particles = [P.u2bar, P.u1, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_225,(0,1):C.GC_226}) 
 
 
V_130 = Vertex(name = 'V_130', 
	 particles = [P.u2bar, P.u2, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_227,(0,1):C.GC_228}) 
 
 
V_131 = Vertex(name = 'V_131', 
	 particles = [P.u2bar, P.u3, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_229,(0,1):C.GC_230}) 
 
 
V_132 = Vertex(name = 'V_132', 
	 particles = [P.u3bar, P.u1, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_231,(0,1):C.GC_232}) 
 
 
V_133 = Vertex(name = 'V_133', 
	 particles = [P.u3bar, P.u2, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_233,(0,1):C.GC_234}) 
 
 
V_134 = Vertex(name = 'V_134', 
	 particles = [P.u3bar, P.u3, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_235,(0,1):C.GC_236}) 
 
 
V_135 = Vertex(name = 'V_135', 
	 particles = [P.d1bar, P.u1, P.Hpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_237,(0,1):C.GC_238}) 
 
 
V_136 = Vertex(name = 'V_136', 
	 particles = [P.d1bar, P.u2, P.Hpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_239,(0,1):C.GC_240}) 
 
 
V_137 = Vertex(name = 'V_137', 
	 particles = [P.d1bar, P.u3, P.Hpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_241,(0,1):C.GC_242}) 
 
 
V_138 = Vertex(name = 'V_138', 
	 particles = [P.d2bar, P.u1, P.Hpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_243,(0,1):C.GC_244}) 
 
 
V_139 = Vertex(name = 'V_139', 
	 particles = [P.d2bar, P.u2, P.Hpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_245,(0,1):C.GC_246}) 
 
 
V_140 = Vertex(name = 'V_140', 
	 particles = [P.d2bar, P.u3, P.Hpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_247,(0,1):C.GC_248}) 
 
 
V_141 = Vertex(name = 'V_141', 
	 particles = [P.d3bar, P.u1, P.Hpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_249,(0,1):C.GC_250}) 
 
 
V_142 = Vertex(name = 'V_142', 
	 particles = [P.d3bar, P.u2, P.Hpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_251,(0,1):C.GC_252}) 
 
 
V_143 = Vertex(name = 'V_143', 
	 particles = [P.d3bar, P.u3, P.Hpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_253,(0,1):C.GC_254}) 
 
 
V_144 = Vertex(name = 'V_144', 
	 particles = [P.nu1, P.nu1, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_255,(0,1):C.GC_256}) 
 
 
V_145 = Vertex(name = 'V_145', 
	 particles = [P.nu1, P.nu2, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_257,(0,1):C.GC_258}) 
 
 
V_146 = Vertex(name = 'V_146', 
	 particles = [P.nu1, P.nu3, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_259,(0,1):C.GC_260}) 
 
 
V_147 = Vertex(name = 'V_147', 
	 particles = [P.nu1, P.nu4, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_261,(0,1):C.GC_262}) 
 
 
V_148 = Vertex(name = 'V_148', 
	 particles = [P.nu1, P.nu5, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_263,(0,1):C.GC_264}) 
 
 
V_149 = Vertex(name = 'V_149', 
	 particles = [P.nu1, P.nu6, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_265,(0,1):C.GC_266}) 
 
 
V_150 = Vertex(name = 'V_150', 
	 particles = [P.nu2, P.nu2, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_267,(0,1):C.GC_268}) 
 
 
V_151 = Vertex(name = 'V_151', 
	 particles = [P.nu2, P.nu3, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_269,(0,1):C.GC_270}) 
 
 
V_152 = Vertex(name = 'V_152', 
	 particles = [P.nu2, P.nu4, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_271,(0,1):C.GC_272}) 
 
 
V_153 = Vertex(name = 'V_153', 
	 particles = [P.nu2, P.nu5, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_273,(0,1):C.GC_274}) 
 
 
V_154 = Vertex(name = 'V_154', 
	 particles = [P.nu2, P.nu6, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_275,(0,1):C.GC_276}) 
 
 
V_155 = Vertex(name = 'V_155', 
	 particles = [P.nu3, P.nu3, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_277,(0,1):C.GC_278}) 
 
 
V_156 = Vertex(name = 'V_156', 
	 particles = [P.nu3, P.nu4, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_279,(0,1):C.GC_280}) 
 
 
V_157 = Vertex(name = 'V_157', 
	 particles = [P.nu3, P.nu5, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_281,(0,1):C.GC_282}) 
 
 
V_158 = Vertex(name = 'V_158', 
	 particles = [P.nu3, P.nu6, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_283,(0,1):C.GC_284}) 
 
 
V_159 = Vertex(name = 'V_159', 
	 particles = [P.nu4, P.nu4, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_285,(0,1):C.GC_286}) 
 
 
V_160 = Vertex(name = 'V_160', 
	 particles = [P.nu4, P.nu5, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_287,(0,1):C.GC_288}) 
 
 
V_161 = Vertex(name = 'V_161', 
	 particles = [P.nu4, P.nu6, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_289,(0,1):C.GC_290}) 
 
 
V_162 = Vertex(name = 'V_162', 
	 particles = [P.nu5, P.nu5, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_291,(0,1):C.GC_292}) 
 
 
V_163 = Vertex(name = 'V_163', 
	 particles = [P.nu5, P.nu6, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_293,(0,1):C.GC_294}) 
 
 
V_164 = Vertex(name = 'V_164', 
	 particles = [P.nu6, P.nu6, P.h], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_295,(0,1):C.GC_296}) 
 
 
V_165 = Vertex(name = 'V_165', 
	 particles = [P.e1bar, P.nu1, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_297,(0,1):C.GC_298}) 
 
 
V_166 = Vertex(name = 'V_166', 
	 particles = [P.e1bar, P.nu2, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_299,(0,1):C.GC_300}) 
 
 
V_167 = Vertex(name = 'V_167', 
	 particles = [P.e1bar, P.nu3, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_301,(0,1):C.GC_302}) 
 
 
V_168 = Vertex(name = 'V_168', 
	 particles = [P.e1bar, P.nu4, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_303,(0,1):C.GC_304}) 
 
 
V_169 = Vertex(name = 'V_169', 
	 particles = [P.e1bar, P.nu5, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_305,(0,1):C.GC_306}) 
 
 
V_170 = Vertex(name = 'V_170', 
	 particles = [P.e1bar, P.nu6, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_307,(0,1):C.GC_308}) 
 
 
V_171 = Vertex(name = 'V_171', 
	 particles = [P.e2bar, P.nu1, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_309,(0,1):C.GC_310}) 
 
 
V_172 = Vertex(name = 'V_172', 
	 particles = [P.e2bar, P.nu2, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_311,(0,1):C.GC_312}) 
 
 
V_173 = Vertex(name = 'V_173', 
	 particles = [P.e2bar, P.nu3, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_313,(0,1):C.GC_314}) 
 
 
V_174 = Vertex(name = 'V_174', 
	 particles = [P.e2bar, P.nu4, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_315,(0,1):C.GC_316}) 
 
 
V_175 = Vertex(name = 'V_175', 
	 particles = [P.e2bar, P.nu5, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_317,(0,1):C.GC_318}) 
 
 
V_176 = Vertex(name = 'V_176', 
	 particles = [P.e2bar, P.nu6, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_319,(0,1):C.GC_320}) 
 
 
V_177 = Vertex(name = 'V_177', 
	 particles = [P.e3bar, P.nu1, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_321,(0,1):C.GC_322}) 
 
 
V_178 = Vertex(name = 'V_178', 
	 particles = [P.e3bar, P.nu2, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_323,(0,1):C.GC_324}) 
 
 
V_179 = Vertex(name = 'V_179', 
	 particles = [P.e3bar, P.nu3, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_325,(0,1):C.GC_326}) 
 
 
V_180 = Vertex(name = 'V_180', 
	 particles = [P.e3bar, P.nu4, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_327,(0,1):C.GC_328}) 
 
 
V_181 = Vertex(name = 'V_181', 
	 particles = [P.e3bar, P.nu5, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_329,(0,1):C.GC_330}) 
 
 
V_182 = Vertex(name = 'V_182', 
	 particles = [P.e3bar, P.nu6, P.Hpc], 
	 color = ['1'], 
	 lorentz = [L.FFS1,L.FFS2], 
	 couplings = {(0,0):C.GC_331,(0,1):C.GC_332}) 
 
 
V_183 = Vertex(name = 'V_183', 
	 particles = [P.d1bar, P.d1, P.g], 
	 color = ['T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_333,(0,0):C.GC_334}) 
 
 
V_184 = Vertex(name = 'V_184', 
	 particles = [P.d2bar, P.d2, P.g], 
	 color = ['T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_335,(0,0):C.GC_336}) 
 
 
V_185 = Vertex(name = 'V_185', 
	 particles = [P.d3bar, P.d3, P.g], 
	 color = ['T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_337,(0,0):C.GC_338}) 
 
 
V_186 = Vertex(name = 'V_186', 
	 particles = [P.d1bar, P.d1, P.A], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_339,(0,0):C.GC_340}) 
 
 
V_187 = Vertex(name = 'V_187', 
	 particles = [P.d2bar, P.d2, P.A], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_341,(0,0):C.GC_342}) 
 
 
V_188 = Vertex(name = 'V_188', 
	 particles = [P.d3bar, P.d3, P.A], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_343,(0,0):C.GC_344}) 
 
 
V_189 = Vertex(name = 'V_189', 
	 particles = [P.u1bar, P.d1, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_345}) 
 
 
V_190 = Vertex(name = 'V_190', 
	 particles = [P.u1bar, P.d2, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_346}) 
 
 
V_191 = Vertex(name = 'V_191', 
	 particles = [P.u1bar, P.d3, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_347}) 
 
 
V_192 = Vertex(name = 'V_192', 
	 particles = [P.u2bar, P.d1, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_348}) 
 
 
V_193 = Vertex(name = 'V_193', 
	 particles = [P.u2bar, P.d2, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_349}) 
 
 
V_194 = Vertex(name = 'V_194', 
	 particles = [P.u2bar, P.d3, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_350}) 
 
 
V_195 = Vertex(name = 'V_195', 
	 particles = [P.u3bar, P.d1, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_351}) 
 
 
V_196 = Vertex(name = 'V_196', 
	 particles = [P.u3bar, P.d2, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_352}) 
 
 
V_197 = Vertex(name = 'V_197', 
	 particles = [P.u3bar, P.d3, P.Wp], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_353}) 
 
 
V_198 = Vertex(name = 'V_198', 
	 particles = [P.d1bar, P.d1, P.Z], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_354,(0,0):C.GC_355}) 
 
 
V_199 = Vertex(name = 'V_199', 
	 particles = [P.d2bar, P.d2, P.Z], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_356,(0,0):C.GC_357}) 
 
 
V_200 = Vertex(name = 'V_200', 
	 particles = [P.d3bar, P.d3, P.Z], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_358,(0,0):C.GC_359}) 
 
 
V_201 = Vertex(name = 'V_201', 
	 particles = [P.nu1, P.e1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_360}) 
 
 
V_202 = Vertex(name = 'V_202', 
	 particles = [P.nu1, P.e2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_361}) 
 
 
V_203 = Vertex(name = 'V_203', 
	 particles = [P.nu1, P.e3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_362}) 
 
 
V_204 = Vertex(name = 'V_204', 
	 particles = [P.nu2, P.e1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_363}) 
 
 
V_205 = Vertex(name = 'V_205', 
	 particles = [P.nu2, P.e2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_364}) 
 
 
V_206 = Vertex(name = 'V_206', 
	 particles = [P.nu2, P.e3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_365}) 
 
 
V_207 = Vertex(name = 'V_207', 
	 particles = [P.nu3, P.e1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_366}) 
 
 
V_208 = Vertex(name = 'V_208', 
	 particles = [P.nu3, P.e2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_367}) 
 
 
V_209 = Vertex(name = 'V_209', 
	 particles = [P.nu3, P.e3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_368}) 
 
 
V_210 = Vertex(name = 'V_210', 
	 particles = [P.nu4, P.e1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_369}) 
 
 
V_211 = Vertex(name = 'V_211', 
	 particles = [P.nu4, P.e2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_370}) 
 
 
V_212 = Vertex(name = 'V_212', 
	 particles = [P.nu4, P.e3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_371}) 
 
 
V_213 = Vertex(name = 'V_213', 
	 particles = [P.nu5, P.e1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_372}) 
 
 
V_214 = Vertex(name = 'V_214', 
	 particles = [P.nu5, P.e2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_373}) 
 
 
V_215 = Vertex(name = 'V_215', 
	 particles = [P.nu5, P.e3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_374}) 
 
 
V_216 = Vertex(name = 'V_216', 
	 particles = [P.nu6, P.e1, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_375}) 
 
 
V_217 = Vertex(name = 'V_217', 
	 particles = [P.nu6, P.e2, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_376}) 
 
 
V_218 = Vertex(name = 'V_218', 
	 particles = [P.nu6, P.e3, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_377}) 
 
 
V_219 = Vertex(name = 'V_219', 
	 particles = [P.e1bar, P.e1, P.A], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_378,(0,0):C.GC_379}) 
 
 
V_220 = Vertex(name = 'V_220', 
	 particles = [P.e2bar, P.e2, P.A], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_380,(0,0):C.GC_381}) 
 
 
V_221 = Vertex(name = 'V_221', 
	 particles = [P.e3bar, P.e3, P.A], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_382,(0,0):C.GC_383}) 
 
 
V_222 = Vertex(name = 'V_222', 
	 particles = [P.e1bar, P.e1, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_384,(0,0):C.GC_385}) 
 
 
V_223 = Vertex(name = 'V_223', 
	 particles = [P.e2bar, P.e2, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_386,(0,0):C.GC_387}) 
 
 
V_224 = Vertex(name = 'V_224', 
	 particles = [P.e3bar, P.e3, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_388,(0,0):C.GC_389}) 
 
 
V_225 = Vertex(name = 'V_225', 
	 particles = [P.u1bar, P.u1, P.g], 
	 color = ['T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_390,(0,0):C.GC_391}) 
 
 
V_226 = Vertex(name = 'V_226', 
	 particles = [P.u2bar, P.u2, P.g], 
	 color = ['T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_392,(0,0):C.GC_393}) 
 
 
V_227 = Vertex(name = 'V_227', 
	 particles = [P.u3bar, P.u3, P.g], 
	 color = ['T(3,2,1)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_394,(0,0):C.GC_395}) 
 
 
V_228 = Vertex(name = 'V_228', 
	 particles = [P.u1bar, P.u1, P.A], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_396,(0,0):C.GC_397}) 
 
 
V_229 = Vertex(name = 'V_229', 
	 particles = [P.u2bar, P.u2, P.A], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_398,(0,0):C.GC_399}) 
 
 
V_230 = Vertex(name = 'V_230', 
	 particles = [P.u3bar, P.u3, P.A], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_400,(0,0):C.GC_401}) 
 
 
V_231 = Vertex(name = 'V_231', 
	 particles = [P.u1bar, P.u1, P.Z], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_402,(0,0):C.GC_403}) 
 
 
V_232 = Vertex(name = 'V_232', 
	 particles = [P.u2bar, P.u2, P.Z], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_404,(0,0):C.GC_405}) 
 
 
V_233 = Vertex(name = 'V_233', 
	 particles = [P.u3bar, P.u3, P.Z], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_406,(0,0):C.GC_407}) 
 
 
V_234 = Vertex(name = 'V_234', 
	 particles = [P.d1bar, P.u1, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_408}) 
 
 
V_235 = Vertex(name = 'V_235', 
	 particles = [P.d1bar, P.u2, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_409}) 
 
 
V_236 = Vertex(name = 'V_236', 
	 particles = [P.d1bar, P.u3, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_410}) 
 
 
V_237 = Vertex(name = 'V_237', 
	 particles = [P.d2bar, P.u1, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_411}) 
 
 
V_238 = Vertex(name = 'V_238', 
	 particles = [P.d2bar, P.u2, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_412}) 
 
 
V_239 = Vertex(name = 'V_239', 
	 particles = [P.d2bar, P.u3, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_413}) 
 
 
V_240 = Vertex(name = 'V_240', 
	 particles = [P.d3bar, P.u1, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_414}) 
 
 
V_241 = Vertex(name = 'V_241', 
	 particles = [P.d3bar, P.u2, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_415}) 
 
 
V_242 = Vertex(name = 'V_242', 
	 particles = [P.d3bar, P.u3, P.Wpc], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_416}) 
 
 
V_243 = Vertex(name = 'V_243', 
	 particles = [P.nu1, P.nu1, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_417,(0,0):C.GC_418}) 
 
 
V_244 = Vertex(name = 'V_244', 
	 particles = [P.nu1, P.nu2, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_419,(0,0):C.GC_420}) 
 
 
V_245 = Vertex(name = 'V_245', 
	 particles = [P.nu1, P.nu3, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_421,(0,0):C.GC_422}) 
 
 
V_246 = Vertex(name = 'V_246', 
	 particles = [P.nu1, P.nu4, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_423,(0,0):C.GC_424}) 
 
 
V_247 = Vertex(name = 'V_247', 
	 particles = [P.nu1, P.nu5, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_425,(0,0):C.GC_426}) 
 
 
V_248 = Vertex(name = 'V_248', 
	 particles = [P.nu1, P.nu6, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_427,(0,0):C.GC_428}) 
 
 
V_249 = Vertex(name = 'V_249', 
	 particles = [P.nu2, P.nu2, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_429,(0,0):C.GC_430}) 
 
 
V_250 = Vertex(name = 'V_250', 
	 particles = [P.nu2, P.nu3, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_431,(0,0):C.GC_432}) 
 
 
V_251 = Vertex(name = 'V_251', 
	 particles = [P.nu2, P.nu4, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_433,(0,0):C.GC_434}) 
 
 
V_252 = Vertex(name = 'V_252', 
	 particles = [P.nu2, P.nu5, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_435,(0,0):C.GC_436}) 
 
 
V_253 = Vertex(name = 'V_253', 
	 particles = [P.nu2, P.nu6, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_437,(0,0):C.GC_438}) 
 
 
V_254 = Vertex(name = 'V_254', 
	 particles = [P.nu3, P.nu3, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_439,(0,0):C.GC_440}) 
 
 
V_255 = Vertex(name = 'V_255', 
	 particles = [P.nu3, P.nu4, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_441,(0,0):C.GC_442}) 
 
 
V_256 = Vertex(name = 'V_256', 
	 particles = [P.nu3, P.nu5, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_443,(0,0):C.GC_444}) 
 
 
V_257 = Vertex(name = 'V_257', 
	 particles = [P.nu3, P.nu6, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_445,(0,0):C.GC_446}) 
 
 
V_258 = Vertex(name = 'V_258', 
	 particles = [P.nu4, P.nu4, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_447,(0,0):C.GC_448}) 
 
 
V_259 = Vertex(name = 'V_259', 
	 particles = [P.nu4, P.nu5, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_449,(0,0):C.GC_450}) 
 
 
V_260 = Vertex(name = 'V_260', 
	 particles = [P.nu4, P.nu6, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_451,(0,0):C.GC_452}) 
 
 
V_261 = Vertex(name = 'V_261', 
	 particles = [P.nu5, P.nu5, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_453,(0,0):C.GC_454}) 
 
 
V_262 = Vertex(name = 'V_262', 
	 particles = [P.nu5, P.nu6, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_455,(0,0):C.GC_456}) 
 
 
V_263 = Vertex(name = 'V_263', 
	 particles = [P.nu6, P.nu6, P.Z], 
	 color = ['1'], 
	 lorentz = [L.FFV2,L.FFV3], 
	 couplings = {(0,1):C.GC_457,(0,0):C.GC_458}) 
 
 
V_264 = Vertex(name = 'V_264', 
	 particles = [P.e1bar, P.nu1, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_459}) 
 
 
V_265 = Vertex(name = 'V_265', 
	 particles = [P.e1bar, P.nu2, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_460}) 
 
 
V_266 = Vertex(name = 'V_266', 
	 particles = [P.e1bar, P.nu3, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_461}) 
 
 
V_267 = Vertex(name = 'V_267', 
	 particles = [P.e1bar, P.nu4, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_462}) 
 
 
V_268 = Vertex(name = 'V_268', 
	 particles = [P.e1bar, P.nu5, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_463}) 
 
 
V_269 = Vertex(name = 'V_269', 
	 particles = [P.e1bar, P.nu6, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_464}) 
 
 
V_270 = Vertex(name = 'V_270', 
	 particles = [P.e2bar, P.nu1, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_465}) 
 
 
V_271 = Vertex(name = 'V_271', 
	 particles = [P.e2bar, P.nu2, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_466}) 
 
 
V_272 = Vertex(name = 'V_272', 
	 particles = [P.e2bar, P.nu3, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_467}) 
 
 
V_273 = Vertex(name = 'V_273', 
	 particles = [P.e2bar, P.nu4, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_468}) 
 
 
V_274 = Vertex(name = 'V_274', 
	 particles = [P.e2bar, P.nu5, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_469}) 
 
 
V_275 = Vertex(name = 'V_275', 
	 particles = [P.e2bar, P.nu6, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_470}) 
 
 
V_276 = Vertex(name = 'V_276', 
	 particles = [P.e3bar, P.nu1, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_471}) 
 
 
V_277 = Vertex(name = 'V_277', 
	 particles = [P.e3bar, P.nu2, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_472}) 
 
 
V_278 = Vertex(name = 'V_278', 
	 particles = [P.e3bar, P.nu3, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_473}) 
 
 
V_279 = Vertex(name = 'V_279', 
	 particles = [P.e3bar, P.nu4, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_474}) 
 
 
V_280 = Vertex(name = 'V_280', 
	 particles = [P.e3bar, P.nu5, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_475}) 
 
 
V_281 = Vertex(name = 'V_281', 
	 particles = [P.e3bar, P.nu6, P.Wpc], 
	 color = ['1'], 
	 lorentz = [L.FFV3], 
	 couplings = {(0,0):C.GC_476}) 
 
 
V_282 = Vertex(name = 'V_282', 
	 particles = [P.g, P.g, P.g], 
	 color = ['f(1,2,3)'], 
	 lorentz = [L.VVV1], 
	 couplings = {(0,0):C.GC_477}) 
 
 
V_283 = Vertex(name = 'V_283', 
	 particles = [P.Wpc, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.VVV1], 
	 couplings = {(0,0):C.GC_478}) 
 
 
V_284 = Vertex(name = 'V_284', 
	 particles = [P.Wpc, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.VVV1], 
	 couplings = {(0,0):C.GC_479}) 
 
 
V_285 = Vertex(name = 'V_285', 
	 particles = [P.g, P.g, P.g, P.g], 
	 color = ['f(-1,1,4)*f(-1,2,3)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,2)*f(-1,3,4)'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_480,(1,0):C.GC_481,(0,1):C.GC_482,(2,1):C.GC_483,(1,2):C.GC_484,(2,2):C.GC_485}) 
 
 
V_286 = Vertex(name = 'V_286', 
	 particles = [P.Wpc, P.A, P.A, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_486,(0,1):C.GC_487,(0,2):C.GC_488}) 
 
 
V_287 = Vertex(name = 'V_287', 
	 particles = [P.Wpc, P.A, P.Wp, P.Z], 
	 color = ['1'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_489,(0,1):C.GC_490,(0,2):C.GC_491}) 
 
 
V_288 = Vertex(name = 'V_288', 
	 particles = [P.Wpc, P.Wpc, P.Wp, P.Wp], 
	 color = ['1'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_492,(0,1):C.GC_493,(0,2):C.GC_494}) 
 
 
V_289 = Vertex(name = 'V_289', 
	 particles = [P.Wpc, P.Wp, P.Z, P.Z], 
	 color = ['1'], 
	 lorentz = [L.VVVV1,L.VVVV2,L.VVVV3], 
	 couplings = {(0,0):C.GC_495,(0,1):C.GC_496,(0,2):C.GC_497}) 
 
 
V_290 = Vertex(name = 'V_290', 
	 particles = [P.A, P.A, P.h], 
	 color = ['1'], 
	 lorentz = [L.VVS99], 
	 couplings = {(0,0):C.GC_498}) 
 
 
V_291 = Vertex(name = 'V_291', 
	 particles = [P.g, P.g, P.h], 
	 color = ['Identity(1,2)'], 
	 lorentz = [L.VVS99], 
	 couplings = {(0,0):C.GC_499}) 
 
 
