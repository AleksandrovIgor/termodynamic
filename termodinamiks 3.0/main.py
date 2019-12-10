# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c_un.ui'
#
# Created: Thu May 13 16:40:36 2010
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from sympy import *
import sys
from interf import Ui_Form



class Formyla(object):

    def vihislis(self, f_la, arg):
        """this function, consider argument (arg), from formula   (f_la)"""
        m =solve(f_la, arg)
        return m[0]


class UUi_Form(Ui_Form):
 
        
#------------------
    def vhodiashie_vozmuhenia(self):

        temperatyra = float(self.lineEdit_2.text())
        davlenie = float(self.lineEdit_3.text())

        
        gaz = self.comboBox.currentText()
        
        kombo_pri_temp = self.comboBox_7.currentIndex()
        kombo_pri_davlenii =self.comboBox_6.currentIndex()
        kombo_idealnost_gaza =self.comboBox_4.currentIndex()
 
       
        print "temperatyra= ",   temperatyra  
        print "davlenie =",   davlenie 
        f = open('zzz.txt')
        p = f.readlines()
 
        for line in p:
            ggg, M, Tc, Pc, Vc, Zc, w, dHof298, Sof298, do, d1, d2, d3 = line.split()
            if ggg == gaz:
                     break
        f.close()

        self.obrabotka(ggg, kombo_pri_temp, temperatyra, kombo_pri_davlenii, davlenie, kombo_idealnost_gaza,
                       M, Tc, Pc, Vc, Zc, w, dHof298, Sof298, do, d1, d2, d3 )
        
#---------------
    def obrabotka(self, ggg, kombo_pri_temp, temperatyra, kombo_pri_davlenii, davlenie, kombo_idealnost_gaza,
                  M, Tc, Pc, Vc, Zc, w, dHof298, Sof298, do, d1, d2, d3 ):
 
     
        if kombo_pri_temp == 1 :
            temperatyra = self.kelvin(temperatyra)
            print u'Температура T=',temperatyra, u'Кельвинов'
        
        if not kombo_pri_davlenii == 0 :
            davlenie = self.paskal(davlenie, kombo_pri_davlenii)

            print u'Давление P=', davlenie, u'Паскаль'
        Pc = float(Pc)
        Pc=Pc*1.013*10**5
        print u'Критическое давление Pc=', Pc,  u'Паскаль'

       
        self.rasshet( ggg,   temperatyra,   davlenie, kombo_idealnost_gaza,
                      M, Tc, Pc, Vc, Zc, w, dHof298, Sof298, do, d1, d2, d3 )


    def rasshet(self, _ggg,   _temperatyra,   _davlenie, kombo_idealnost_gaza, _M, _Tc,
                 _Pc, _Vc, _Zc, _w, _dHof298, _Sof298, _do, _d1, _d2, _d3 ):
        formyla = Formyla()
  
        Rm, R, M, poid, P, T, A  = symbols('Rm', 'R', 'M','poid', 'P', 'T', 'A')
        b10, b11, b12, b13, Tc, Pc, w, Tr, Tc, B, z0,z11,z12,z,po  = symbols( 'b10', 'b11', 'b12', 'b13', 'Tc', 'Pc', 'w',' Tr', 'Tc',
                                                                               'B','z0','z11','z12','z','po'  )

        M, Tc, Pc, Vc, Zc, w, dHof298, Sof298,	do, d1, d2, d3 = symbols('M, Tc, Pc, Vc, Zc, w, dHof298, Sof298, do, d1, d2, d3')
        T = _temperatyra
        P = _davlenie
        R = 8314
 
        ggg = _ggg
        M=_M
        Tc = _Tc
        Pc = _Pc
        Vc = _Vc
        Zc = _Zc 
        w = _w
        dHof298 = _dHof298
        Sof298=_Sof298
        do = _do
        d1 = _d1
        d2 = _d2
        d3 = _d3
        #------------------------
        M = float(M)
        Tc = float(Tc)
        Pc = float(Pc)
        Vc = float(Vc)
        Zc = float(Zc)
        w = float(w)
        dHof298 = float(dHof298)
        Sof298 = float(Sof298)
        do = float(do)          
        d1 = float(d1) 
        d2 = float(d2)
        d3 = float(d3)
        #------------------------
 
        print _temperatyra , _davlenie
#        print kombo_pri_temp, kombo_pri_davlenii,
        print kombo_idealnost_gaza       
        print 'ggg',  ggg
        print '_M',  M
        print 'Tc', Tc
        print 'Pc', Pc
        print 'Vc', Vc
        print 'Zc', Zc 
        print 'w', w
        print 'dHof298', dHof298
        print 'Sof298', Sof298
        print 'do', do
        print 'd1', d1
        print 'd2', d2
        print 'd3', d3

        
        formyla = Formyla()
        
        if kombo_idealnost_gaza ==0:
            print 'idealnost_gaza = idealnii'
            print '-------------------------'            
            f_la_rm = Rm-R/M
            Rm = formyla.vihislis(f_la_rm, Rm)
            print 'Rm=',Rm, u'Дж/(кг*К)'

            f_la_poid = poid-P/(Rm*T)
            poid = formyla.vihislis(f_la_poid, poid)
            print 'poid=',poid, u'кг/м3'
            print '-------------------------'           
        #1---------------------
        elif kombo_idealnost_gaza ==1:
            print 'idealnost_gaza = ne idealnii'
            print '-------------------------'  
            
            
            f_la_rm = Rm-R/M
            Rm = formyla.vihislis(f_la_rm, Rm)
            print 'Rm=',Rm, u'Дж/(кг*К)'
            f_la_tr = Tr- T/Tc
            Tr = formyla.vihislis(f_la_tr, Tr)
            print 'Tr=',Tr
            #2---------------------



            f_la_poid = poid-P/(Rm*T)
            poid = formyla.vihislis(f_la_poid, poid)
            print 'poid=',poid, u'кг/м3'


            f_la_b1 = [b10-(Rm*Tc/Pc)*(0.1445+0.0637*w),b11-(Rm*Tc/Pc)*(-0.330), b12-(Rm*Tc/Pc)*(-0.1385+0.331*w), b13-(Rm*Tc/Pc)*(-0.0121-0.423*w) ]

            b10 = formyla.vihislis(f_la_b1[0], b10)
            print 'b10',b10, u'м3/кг'
            b11 = formyla.vihislis(f_la_b1[1], b11)
            print 'b11',b11, u'м3/кг'
            b12 = formyla.vihislis(f_la_b1[2], b12)
            print 'b12',b12, u'м3/кг'
            b13 = formyla.vihislis(f_la_b1[3], b13)
            print 'b13',b13, u'м3/кг'



            #3---------------------
            f_la_B =-B+ b10+b11*Tr**(-1)+b12*Tr**(-2)+b13*Tr**(-3)
            B = formyla.vihislis(f_la_B, B)
            print 'B',B, u'м3/кг'

            #4--------------------- 

            f_la_z0 =-z0+1+B*poid
            z0 = formyla.vihislis(f_la_z0, z0)
            print 'z0=',z0
            #5--------------------- 
             

            f_la_z11 = -z11+ 0.5+(0.25+B*poid)**0.5
            f_la_z12 = -z12+0.5-(0.25+B*poid)**0.5
            z11 = formyla.vihislis(f_la_z11, z11)
            z12 = formyla.vihislis(f_la_z12, z12)
            print 'z11=',z11
            print 'z12=',z12

            #vibrat---------------
            if z0*0.05 > z11-z0:
                z = z11
            
            elif z0*0.05 > -(z11-z0):
                z = z11
 
            elif z0*0.05 > z12-z0:
                z = z12
 
            elif z0*0.05 > -(z12-z0):
                z = z12
            print u'выбираю из 2х z1i близкое к 0-му приближению' 
            print u'z1=', z
            #6--------------------

            f_la_po = -po+poid/z
            po = formyla.vihislis(f_la_po, po)
            print 'po=',po, u'кг/м3'
            #---------------------
            print '-------------------------'  





#---------------
            
    def kelvin(self,t):
        t = 273+t
        return t
#---------------    
    def paskal(self, p, kombo_pri_davlenii):
        if kombo_pri_davlenii == 1:
            p=p*1000
        elif kombo_pri_davlenii == 2:
            p=p*10**5
        elif kombo_pri_davlenii == 3:
            p=p*101325
        elif kombo_pri_davlenii == 4:
            p=p*98066.5
        elif kombo_pri_davlenii == 5:
            p=p*133.322
        elif kombo_pri_davlenii == 6:
            p=p*9806.65
        elif kombo_pri_davlenii == 7:
            p=p*6894.76
        return p
#---------------        

 




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = UUi_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()

 
    
    c = app.exec_()
    
    sys.exit(app.exec_())



