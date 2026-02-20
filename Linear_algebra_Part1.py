# matrix in the form of row and column combine form matrix
# special type of matrixes or Types of matrix
"""
# square matrix means m = n now of rowss == no of columns ismee element equal ho ya na ho koi farakaa nhi padta sirf order equal hona chaihiye
# rectangular matrix m !=n like 1X2 , 2X3 jisme order same na ho
# diagonal = > diagonal me non zero and baki sare zero like diag[1,2] , diag[1,2,3] we also write this as like this
#scaler matrix is combination of  both square + diagonal in which a matrix should be satisft the square matrix condition + also the diagonal matrix condition known as scaler
# Next matrix is Unit Matrix or identity matrix I =  meanns a matrix that is square + diagonals all elements are one
# Null matrix /void/empty =  all elements should be 0 square ka farak nahi padta
# uppertrangular matrix -> ek aisi square matrix jisme diagonal ke ueper wale sare elements non zero hon baki zero hote hai
# lowertrangular matrix -> ek aisi square matrix jisme diagaonal ke niche wale sare elements non zero hote hain and baki uper wale sare zeroes
#idempotent matrix -> when we square the matrix with itself and that same matrix come called this then like Asuare  = A
# involunatary matrix = > asquare = I
# nilpotent matrix  - Ax = 0 (x hai uski power a ki power x ) matlab x ko pehle 1 rakhenge phir 2 jab tak vo 0 ke equal nahi hota tab tak ham kerenge jab vo zero aa gya nilpotent matrix aa jayegi
#Singular matrix jisme jis matrix ka determinant 0 ke qequal ke aa jaye
# row matrix jisme rows ho column na ho same with columns jisme columns ho rows na ho
# equality matrix jisme order and eleements dono same ho
# and one more that is eqvivalence matrix  jise element se farak nahi padta bus uska order same hona chaihiye
"""
#Lecture 2: opeartions on matrix right
"""
# addition ab addition me pata hai order same hoana chaiye verna addition hona possible nahi
#iski properties 1.commutative agar pehlie matrix me dusri add ker du ya dusri me pehlie answer will be same
#2. asssociative = > me pheli do ko pehle add kero then us ke result ko teesri se add kero ya dusre + teesri ko add kerke result ko pehli se add kero ans will be same
#3. additive identity agar ham matrix a me null matrix (0) yani ki zero ko add kerte hai and vahi same matrix A aa jati hai ya fir null matrix (0) me A ko add kerke same A aa jaye to use additive identity kehte hai
#4. Additive inverse => agar kisi matrix me uski  negative matrix add kerde or resiult zero aa jaye to us matrix ko ham additive inverse kahenge
# cancellation  = > isme agar A matrix me X add kerte hai and B me X add kerte hai and cancel out hoke A=B ke aa jata hai  to use cacnellation  kehte hai
"""
# Next hai Substraction
"""
similar hai additino ke jaise bus sign changed hai sirf yaha pe substraction aa jayegi kaise A-b = A +(-B)
# Baki sare rules me bhi yahi cheej hai
# Then atti hai haari multiplicataion by scaler jab kisi matrix ko ham kisi scaler se multiply ker dete ai har ek element .
# isme bhi 4  ways  hai like let the scaler would be k so k(A+B) = kA+kB
# 2-> (p+Q)A = pA +qA   , 3=> p(qA) = (pq)A     ,4 = -kA = k(-A)
"""
# Multiplication
"""
 me jab tak ist matrix me columns ka order equal nahi hota second row ke row se tab tak vo matrix mulitplication nahi keregi no of columns of ist column = no of row of second matrix
# properties ->1) Not commutative  then , A(B+C) = AB +AC tot heek hai tjhen AB = AC => so cancelation will be  B=C theek hai then AIn = InA = A
# if AB = Null(0) Ao 0 B - 0 not always and next will be Atothepowerm . Atothepowern = Atothepower(m+n)
"""

# Lecture 3:
# Trace matlab hota hai jab hamdiagoanls elements ko plus kerdete hain then vo trace nikal jata hai
# peroperties
"""
Tr(ScalerMatrix . AMatrix) = Scalaer MAtrix.TraceofA
Tr(A+B) = TrA+TrB
Tr(AB) = Tr(BA)

Transpose matlab row ko column me and column ko row me simple
Properties
kisi Transpoe matrix ka again transpose ker denge to vo usi ke equal aaa jayagi matlab orignal amtrix ke A
A+B ka tranpose keroge ya phir A ka tranpsoe kerke and B ka transpoe kerke dono ko plus kerenge result will be same
Kisi scaler quanityt ko kisi matrix se ultiply kerke uska tranpose nikalenge ya phir kisi matrix ka tranpose niklake usko scaler quantity se multiply kerer result will be same
ABCka tranpsoe  = C tranpsoe .B tranpose . A tranpose similar with ABtranpsoe = B tranpose A tranpose and also with ABCD tranpsoe = Dtr.Ctr.Btr.Atr

Conjugate of Matrix
when the iyota comes in our matrix its enter in conjugate right  so
for this we change the sign if that is plus cchange to minus or vice versa of that value which contains iyota not real values okey
Properties :
A cponjugae  = A always if that matrix has not any iyota presnet in that matrix only real matrix beaucse no sign chagen so A= A
(A+B)whole ka conjugate  = A con+Bconj
kisi scaler ko Amatrix se mulitply kerke uska conjugate nikalnge sath me ya fir kisi matrix ka conjugate nikalke usme scaler mulitply kerenge both will be same
(AB) = Acon.Bcon
Aconjugate = A for real and Aconj = -A fr pure imaginary in whicih iyota is come

Trapsoe conjugate in which first sign change tehen tranpose okey
ek A matrix hai sabse pehle usme real number ko chod ke baki imaginary nube rme sign change ker do then row ko column and column ko row ker do simple
Properties
A ki tranpose conjugate is always equal to A
A+B ka whole transpose canjugate always equal to A tranpose conjugate + B tranpose conjugate
scaler se A ko mulitply ker ke tranepose conjugate nikalenge ya fir scaler quantity ko ksisi A ke tranpsoe conjugate se mulitply ker do result will be same
AB whole conjugate tranose  = BTranpose Conjugate.A Tranpsoe conjugate
"""
#Lecture 4 Real matrices Symmetrix and skew matrixes
"""
Symmetrix matrix jab kisi matrix ka tranpose usi matrix ke equal aa jaye matlab A transpose  = A Ex identity matrix
Peroperties :
A.Atr = always symmetrix
A+Atr/2  =  always symmetrix
IF A and B are symmetrix then A+B and A-b are also symmetrix and But AB and BA MAy be or may note be right

Skew matrix jab Atr = -A ke equal aa jaye so A-Atr2 is always skew symetrix
A+Atr/2 +A-Atr/2 = A
   S      SS

Orthogonal matrix => Jab kisi Matrix A ka transpose usi ke inveerse ke equal aa jaye  Atr = Ainverse
A.Atr =  A.Ainverse  = I
For Orthogonal matrix A.ATr = I
IF A and B are orthogonal and Ab and Ba are orthogonal
IF orthognola matrix are there so this is  confirm that that determinla will always +-1 but ytou never cant say this that if a matrix have +-1 determinant then that will be orhthogonal matlab vice versa possible nahi hai
"""
#Lecture 5: Complex Matrices
"""
1. Hermitian matrix  kisi matrix ka conjugate tarnpose usi matrix ke equal aa jaye to vo hermitian matrix AconjTr = A
2.Skew hermitian matrix me AconjTr = -A
3. Unitary matrix jisme AconjTr = Ainverse ke equal aa jaye
AAconjTr = AconjTr.A = I
Propertioes
A+B ka whole conjTr = AconjTr+BconjTr
AB)conjTr = BconjuTr.AconjTr

imp=> For herimtiann matrix it is neccessary that all the diagonals elemens willl be real numbers okkey
impo => For skew herimitian maatrix the all digaonal elements either 0 or pure imaginary means associate with i ( iyota )
imp=> A = H+SH = > i/2(A+AconTr) + 1/2(A-AconjTr)
imp=>For unitary matrix the deleterminant of Amodulas will alwayhs be 1 not +-1 okey
"""
#LEcture 6
"""
in 2x2 matrix we multiply diagonal element and subtract them like A determinant =  ad-bc but in 3X3 matrix
There we found the determinant with the help of 6 ways rememebr alywas this short method
+ - +  ye apni row ist hai agar horizonaly dekhe to or agar vertically dekhe +-+ to columnbhi row ist aise kerke 6 tareeke se ham in signs se determniant nikal sakte hai
- + -
+ - +
Now cofcator and minors
agar 2X2 matrix hai to minors bhi 4 honger and cofactros bhi to minors in case of 2x2 matrxi hai elements khud and cofactor me jaha pe even hai vo same or jaha pe odd hai vaha sign change liek A12 =  A3 means odd so sign change ex tha
agar 3X3 matrix ki bat ho rhi hai to vahi ham coffactor nikalnege 9 to har ek coffactor determniant ke roop me niklage and baki sign wala lfda to same hi hai cofactors me odd me position me sign change  ho hata hai  but even pe same rehta hai and minros vaise ke vaise rehte hain right
"""
#Lecture 7: Properties of Determinant
"""
1. Agar kisi matrix ka detminant nikalu to vo always us matrix ke tranpose ke determninant will be equal
2. If two rows  or columsn of a determniant interchange the sign of det is changed like 2 in left side so -2 is in right side okey just Ex.
3. IF any two rows or columns adre identical then determinant is Zero
4. agar kisi A matrix ko scaler se multiply kerenge then uska determinant nikalnge  to vo always  =  kisi scaler ke n power matlab jis order me A matrix hai .A ke determinant ke okey
5. if corrosnpoonding elemetns of any row roys or column are proeroption then determinant will be zero matlab like pehli row hai 1 2 3 and second row hai 1 9 12 and 3 row hai 4 8 12 so agar mai 3 row se 4 common le lu to exect ist row bun jayegi anad ist and 3rd row identical ho jayengei
Note main cheej jab ham kisi scaler ko kisi amtrix se multiply kerte hai to vo us matrix ke sare elements se mulitply hotihai but aga rham comon lete hai to hamari marji hai row ist se le second se le ya fir 3rd se
6. | a+b   g   j |
| c+d   h   k |
| e+f   i   l |
 =

 | a   g   j |   +   | b   g   j |
| c   h   k |       | d   h   k |
| e   i   l |       | f   i   l |
"""
#Lecture 8. Adjoints and its properties
"""
FIRST REMEMBER THIS THING FROM LECTURE 8 TO fURTHER ON ->  HAMNE SIRF MAIN THING READ KI HAI LEANR KI HAI PROPEROTES PE DHAYAN NAHI DIYA KUNKI MUJHE LAGA NAHI KI ABHI PADHNA IMPORTANT HOGA RIGHT TO JO CHEEJ IMPORTANT THI THAT I GOT IT ALREADY OKEY
adjoint hamne solve ker hi liya tha then
"""
# Lecture 9. inverse and its properties
"""
Yeh bhi hamne litlle bit dekh liya tha jitna jarrorit tha
"""
# Lecture 10: non homogenous matrix
"""
same this one yeh bhi solve kuiya th and iska chart banaya tha no soolution unique solution ka
"""
#Lecture 11: homogenous matrix
"""
same this one isme hamne trivial and noon trivial ka chart banaya tha aand isme solution hamesha consistent trahega but in non me may be or not be
"""
#Lecture 12: Rank of matrix :
"""
So in this one sabse pehlee rank basic method se kaise nikalte hain jitne bhi order ki matrix hoti hai like 4X4 ,3X3 ... ,  to us matrix ka det nikalte hain let suppose 3by3 ki hai or uska det 0 aa gya to ham kahenge ki hamar rank<3 hai
3 builkul nahi hoga then ham 2by2 check kerenge har possible 2by2 order matrix us 3by3 order matrix me and agar usme bhi koi bhi non zero nahi aya to one by one check kerenge to one by one me to simple hogya ki rank one hai
but agar 2by2 me non zero element aa jata hai to matlab matrix ka rank 2 hai and 3 by 3 me koi agar non zero ata haii to matlab matrix ka rank 3 hai right understand
"""
#Lecture 14 Rank of matrix findby the help of Euclear form :
"""
Ab sabse pehle hame matrix koo row euclear form me convert karna padega ya phir column euclera form me ab jo row euclean form hai vo kya kehti hai ki har row me jo pehla non zero element hoga that always be start with 1 that is must
and vo ek or cheej khehti hai ki always jo non zeroes elements hai har row me to succesor row me non zero element yani ki 1 se pehle 0s precidor row se jyada hogi yani ki jaise ist row me 1 se pehle ek bhi 0 nahi hai to second me ek 0
aa jayegi third me 2 aa gayi 4th me 4 aagayi matlab badni chaiye to ye hai apni row euclean form ka strucutre
Next jab ham iska numerical solve kerte hai to always ham kya kerte hain ki oeparionts lagate hai taki us matrix ko ham row euclear form me convert kersake jiski bat mai uper structure me kerchuka hu already okey and jab at last me ham
Matrix ko row euclear form me convert kerlenge tab jitni non zeroes row bachengi vo uski rank hogi and THIS IS THE RANK FINDING METHOD WITH THE HELP OF ROW EUCLEAR FORM NEXT IS OUR  NORMAL FORMA OKEY
"""
#Lecture 14 Rank of matrix findby the help of Normal form:
"""
So in Normal form or we say Conical form: To is method me ham kya kerte hia so suppose we given a matrix to ham try kerenge ki usme identity matrix then baki sari ki sari null matrix bane and finally jitne order ki identity matrix nikal
ke ayegi vo order hamare matrix ki rank kehlayegi okey so this is also the method but for the coding pov we dont want to implement the every method because in librrary i sure there is smoe one good and efficient way to solve this question
we only discuss these all methods beccause we atleast know that what is these all things okey
"""
#lecture 15 System of Non Homogenous linear equations With the help of the rank method:
"""
To this lecture will solve the non homogenous liner eqn with the help of rnak method to sabse pehle hame kya kerna hai let suppose hame ek matrix de rakhi hai right or uski row kuch aise hogi like ax +by +cz = n so we convert the every row of
the matrix into like this ax+by+cz : n matlab argumented row (:) iska matlab right so matlab hame is formate me apne matrix ko banana hai in form of A: B like this
[ 1  -1   1 |  2 ]
[ 0   1   0 |  2 ]
[ 0   0   1 | -7 ]

Now hame man lo koi question liya jata hai 3 equation di hai and hamne usme row euclear form laga ke hamne us row ko puri trah convvert ker diya and final result ye uper di gyi matrix ayi right now iski rank kitni hai 3 kunki non zeroes rows
kitni hai 3 and agar ham 2 2 -7 ki bhi sath me leker chek kere to bhi vo rank 3 hi rahegi now iske bad hame 3 rules yad rakhne hai
p(A) !=P(A:B) so the systtem is inconsistent matlab no solution
p(A) = P(A:B) = n matlab the system is consistent matlab unique solution
p(A) = p(A:B)<n matlab the system is consistent but the infinite solution right

now at last hame x y z ki value bhi nikalni padegi to
look at the matrix
look third row  x(0)+y(0)+z(1) = -7 matlab z = -7
look second row x(0)+y(1)+z(0) = 2 matlab y = 2
look ist row x(1)+(2)(-1)+1(-7) matlab x = 11 yaha se sari values aa jayegi to yeh hamara rank method of finding the non homogenous solution for the linear equation next rahega hamara Homogeneous with the help of rank method
"""
#Lecture 16: System of Homogenous linear equation with the help of the rank method  :
"""
Kuch ni yar isme kya hai ki A hoga the B to hamrai zeroes hi hoti hai kunki  = 0 matlab hi homogenous hota hai then X hoga unknown variable like x y z to ham kya kernge ki ek matrix ko row euclear form me covnert kernege
then uski rank nikalnege vahi same way but the catch here is isme 2 hi rules follow honge
pehla agar rnak  = n ke ati hai matlab rank uski matrix ki highest matlab order ke equal like 3 by 3 ki hai to rank 3 aa jati hai to matlab vo unique solution ya ham trivial soltuiont bhi keh sakte hai jise kitne bhi solution niklal lo 0 ke
qeual ayenge matlab uniquely solutions okeey
Then second is our infinite solution jise agar P(A) <n aa gayi to us case me infinite soluion  banenge and is case me hamesha determniant of matrix jo hai hamra zero rahega right
"""
#Lecture 17: Chracterstici matrix, chracterstic polynormail ,chraterstic equn and crhacterstics roors :
"""
very simple hai yar hame ek equation di hogi right usko ksime convert kerta hai uske diagonal elements ko lemda se minus kerdena hai like A-lemdaI then ise ham kehte hain ch.matrix right 2. next hai hamara ch. polynormail agar ham |A-lemdaI| ham ch.matrix
ka det nikal lete hai to vo kehlata hai ch poluynormail right 3. ch equation |A-lemdaI| = 0 ke rakh denge to ch equation 4. ise solve kerne ke bad 3 ko jo values niklene use eigen values ya ch roots kehenge 5. last and final spectrum sab roots ya sari eigen values
ko ham ek set me ikatha ker ke likh de to unhe ham spectrum bolenge simple right like{1,2,3}
"""
#Lecture 18:
"""
A = | 1   2   3 |
    | 0  -4   2 |
    | 0   0   7 |

| 1-λ   2    3 |
|  0  -4-λ  2 | = 0
|  0    0  7-λ |

(1-λ)[(-4-λ)(7-λ) - 0] = 0

(1-λ)(4+λ)(7-λ) = 0

λ = 1 , -4 , 7
λ₁ = 1

| 0   2   3 |   | x₁ |   | 0 |
| 0  -5   2 | * | x₂ | = | 0 |
| 0   0   6 |   | x₃ |   | 0 |

6x₃ = 0  →  x₃ = 0
-5x₂ + 2x₃ = 0  →  x₂ = 0
2x₁ + 3x₃ = 0

x₁ = k
λ₂ = -4

| 5   2   3 |   | x₁ |   | 0 |
| 0   0   2 | * | x₂ | = | 0 |
| 0   0  11 |   | x₃ |   | 0 |

11x₃ = 0  →  x₃ = 0
5x₁ + 2x₂ + 3x₃ = 0
5x₁ + 2x₂ = 0

x₂ = -5h/2
k = | 1 |
    | -5/2 |
    |  0  |
"""
#Finish 
# first we compplete the  READING PART now we start the implementation part okey 
#This block is for code th4e upper definnation because here we do all the implementations okey
#1. To write a matrix
import numpy as np
matrix = np.array([[1,2,3],[2,3,4],[4,5,6]])
matrix
rectangular_matrix = np.array([[1,2,3,4],[1,2,4,5]]) # 2X4 2 Rows and 4columns
rectangular_matrix
diagonal_matrix = np.diag([1,2,3])
diagonal_matrix
scaler_matrix = 3*np.eye(4) # np.eye make the identity matrix and outer 3 multiply this into scaler that is 3 to all the diaogonals
scaler_matrix
Null_matrix = np.zeros((5,4)) # zeroes matlab ek zeores ka matrix create kerta hai right
Null_matrix
upper_triangular_matrix = np.triu(matrix)
upper_triangular_matrix
lower_triangular_matrix = np.tril(matrix)
lower_triangular_matrix
idempotent_matrix = np.allclose(matrix @ matrix, matrix)
idempotent_matrix
if np.allclose(idempotent_matrix,matrix): # idempotent_matrix here is A² and right side is A
    print("Idempotent")
else:
    print("Not Idempotent")
involuntary_matrix = np.array([[1,0],[0,1]])
involuntary_matrix
nipolent_matrix  = np.array([[0,1],[0,0]])
nipolent_matrix
nipolent_matrix @ nipolent_matrix # matlab tak tak muliply kerenge jab tak zero nahi aa jate rught
singular_matrix = np.linalg.det(matrix)
singular_matrix # jis matrix ka determniant 0 aa jaye to vo singular_matrix hoti hai
row_matrix = np.array([1,2,3])
row_matrix
column_matrix = np.array([[1],[2],[3]])
column_matrix
A =  np.array([[1,2,3],[2,3,4],[4,5,6]])
B = np.array([[1,2,3],[2,3,4],[4,5,6]])
if np.allclose(A,B):
    print("Equal")
else:
    print("Not Equal")
if A.shape == B.shape:
    print("Equal")
else:
    print("Not Equal")

#Lecture 2:
C= np.add(A,B)
C
S = np.subtract(A,B)
S
zero_matrix = np.zeros((3,3))
if np.array_equal(A+zero_matrix, zero_matrix+A):
    print("aditive identiy")
else:
    print("Not")
a =  np.array([[1,2,3],[2,3,4],[4,5,6]])
b = np.array([[1,2,3],[2,3,4],[4,5,6]])
zero_matrixfor_inverse = np.zeros_like(a) # ye same shape and size ka zoeres matrix bana deta hai
if np.array_equal(a+(-b),zero_matrixfor_inverse):
    print("aditive inverse")
else:
    print("not aditive inverse ")
cancelation_a =  np.array([[1,2,3],[2,3,4],[4,5,6]])
cancelation_b = np.array([[1,2,3],[2,3,4],[4,5,6]])
z_zero = np.zeros((3,3))
if np.array_equal(cancelation_a + C , cancelation_b +C):
    print("cancelation")
else:
    print("not cancelation")
#Substractino and Multilication same jaise hai to use nahi kerte next hai lecture 3
# lecture 3: Trace
trace_A = np.array([[1,22,3],[22,3,4],[4,5,66]])
print(np.trace(trace_A))
# now in this linear algebra till now there is only few 5 topics in which we use the real life code exampler to understnad the further topics that is 
