
# # WHEN YOU UNLOCK THE GAME, IN THE SAME TIME U UNLOCK THE THE DISK TO USE # #

import io, sys # UTF8_Characters
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from subprocess import call
import time 
import cowsay

# Colors 
COLOR_BANNER = '\033[0;36m'
COLOR_BANNER1 = '\033[1;36m'
COLOR_BANNER2 = '\033[1;31m'
COLOR_BANNER3 = '\033[1;32m'
COLOR_BANNER4 = '\033[0;33m'
COLOR_BANNER5 = '\033[1;33m'
COLOR_BANNER6 = '\033[0;35m'
COLOR_BANNER7 = '\033[1;35m'
COLOR_BANNER8 = '\033[1;34m'
COLOR_BANNER9 = '\033[1;30m'
COLOR_BANNER10 = '\033[1;37m'
COLOR_BANNER_END = '\033[0;m'

print("""


          ,~-.
         (  ' )-.          ,~'`-.
      ,~' `  ' ) )       _(   _) )
     ( ( .--.===.--.    (  `    ' )
      `.%%.;::|888.#`.   `-'`~~=~'
      /%%/::::|8888\##\
     |%%/:::::|88888\##|
     |%%|:::::|88888|##|.,-.
     \%%|:::::|88888|##/    )_
      \%\:::::|88888/#/ ( `'  )
       \%\::::|8888/#/(  ,  -'`-.
   ,~-. `%\:::|888/#'(  (     ') )
  (  ) )_ `\__|__/'   `~-~=--~~='
 ( ` ')  ) [VVVVV]
(_(_.~~~'   \|_|/   hjw
            [XXX]
            `---`

	""")

signStart = ' ▶'
puntEnd = '...'


saludo = " Hi! welcome to the game "
text = "Start ? Yes / No" 
cont = 0
cont2 = 0
cont3 = 0


# Saludo inicial

call('clear')

def iconTriang():
		while True:
			time.sleep(1)
			print("\n")
			print(signStart, end = " ", flush = True)
			break

def pointsCont():
	cont2 = 0
	while cont2 < len(puntEnd):
		time.sleep(1.4)
		print(puntEnd[cont2], end="", flush = True)
		cont2 = cont2 + 1


iconTriang()
while cont < len(saludo):
	time.sleep(0.05)
	print(saludo[cont], end="", flush = True)
	cont = cont + 1


pointsCont()
iconTriang()

while cont3 < len(text):
	time.sleep(0.05)
	print(text[cont3], end="", flush = True)
	cont3 = cont3 + 1



print("\n")

qr = input("  ",)
call('clear')
print("\n","", signStart, qr, end="")





if qr == "yes":
	print("""

                                                  *#.,,,,,,,,,,,,.,&,,,,,,@
                                               @.,,,,,,,,,,,,,,,,,,,,,.@,,,,,,@  *(,
                                           @.,,,,,,,,,...,,,,,,,,,,,,,.,.&,,,,,,,,@.,,,,,&
                                        %,,,,,.,*.,,,,.,,,,,.(,,,,,(*..,,,.%,,,%,.,,,..,,,,&
                                      &,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,,,,,.*,,.,,,.@,,,,,,.
                                    @,..#.,,,,,..,...,,,,,,,,,,,.@.,,,...,,,,,,,&,(,,,,,.#,,,.
                                  %,,,.,,,,,,,,,@       ,,,,,,,,,,*..,.,,,,,,,,,,/,@,,,,,,.,,,..
                                 ..*,,.,,,,,,.(           %.,,.,,,,,,/.,,,,,,,.,,,,,*,.,,,,,,,.,..
                              (,,,,,,,,,,,,.@               &,,,,,,,,*.,,,,,,,,,,,,.*,,,,,,,,,,,,,*
                            &,,,,,,,,,.,,.@                  **,,,,,,,(,%.,,,,,,,,,,/.,,,,,,,,,,,,,/
                           ,,,,,,,.,,,,&*                      *.,,,,,.,/,%.,,,,,,,,,##,,,,,,,,,,,,,@
                         ..,,,,,,,&(.%                           @.,,,...&,,%.,,,,,,,,.,,,,,,,,,,,,,.*
                         .,,.@,,,,.,,              %%              @,,,.,(.,,,..,,,,,,,,,,,,,,,,,,.///&(
                        ,,,%,,,,,,.,,       ,  ,  %%&//             &,,.,,,,.@.,/,,,,,&.,,,,,,,.@&&&////
                       .,#.,,,,,,,#,,	    ,, ,, &,,&/            #/(*,,,,,,@,,.%,,,&.,,,,..#&&&///////
                     /..#,.,,,.,,.,,,         /  ####%%            ,.,,,.,,&.,,,../,..,,%&&&///////@(((&
           ,%&%,@/( &,,.,,,,,,,&#,,,(         /%%####%%            @.((,,,,.,,,,,,(,,,&#/////////////#%
       (&#/////////(*,,,,,,,,,,.,,,,@             ,#*%%/           .,,,,,,,,%.%//#.,./%//////////(&((&
          .%//////&,,,,,,,,,,,,.,,,,*             #,#%             %..,,,,,,,%,%(&/////%///////////////%(
         (////////,,,,,.,,,,,,,,/,,,#              # #             *(,,.,,,,,,*.%/////#///////////////#((@@
           #//////////&((&.,,,,#,,,,*              # %             %..,,,,,,,%,%(&/////%///////////////%($$**
        ///////##////(//@%//##&(%(((*             ***((            #%**#.,,,,.,./#/////////##////(//@%//##&(%(((*
        .///////////#(((((((*/,,/(&&,@*,*****,,*****************.,,,.%((((((((##////////////@/&#(&&%%%#((*&
       /(( /////////&(((((@&&.....(,.&##(********************&.,,,,.,,/((((&%@/((//@////&#(((##(((@#(((((
          @%.  (/, #&&%%&            ,,,//(((/*******%###%#/.      *,#(%,  ((/@((/#(%#(#((((((#(@((#((@((
                &.                                                        .* (& &@  #%  &@



		""")
time.sleep(0.05)	
text = "\n You be in a cave without light, \n only having a lit matchstick. \n  What do you should to do?\n"
print(text.upper(), flush = True)

print(signStart, "Wait there alone")
print(signStart, "Find a door")
print("\n")
sec1 = input(" ",)

if sec1 == "1":
	call('clear')
	print("""

                                                  *#.,,,,,,,,,,,,.,&,,,,,,@
                                               @.,,,,,,,,,,,,,,,,,,,,,.@,,,,,,@  *(,
                                           @.,,,,,,,,,...,,,,,,,,,,,,,.,.&,,,,,,,,@.,,,,,&
                                        %,,,,,.,*.,,,,.,,,,,.(,,,,,(*..,,,.%,,,%,.,,,..,,,,&
                                      &,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,,,,,.*,,.,,,.@,,,,,,.
                                    @,..#.,,,,,..,...,,,,,,,,,,,.@.,,,...,,,,,,,&,(,,,,,.#,,,.
                                  %,,,.,,,,,,,,,@       ,,,,,,,,,,*..,.,,,,,,,,,,/,@,,,,,,.,,,..
                                 ..*,,.,,,,,,.(           %.,,.,,,,,,/.,,,,,,,.,,,,,*,.,,,,,,,.,..
                              (,,,,,,,,,,,,.@               &,,,,,,,,*.,,,,,,,,,,,,.*,,,,,,,,,,,,,*
                            &,,,,,,,,,.,,.@                  **,,,,,,,(,%.,,,,,,,,,,/.,,,,,,,,,,,,,/
                           ,,,,,,,.,,,,&*                      *.,,,,,.,/,%.,,,,,,,,,##,,,,,,,,,,,,,@
                         ..,,,,,,,&(.%                          @.,,,...&,,%.,,,,,,,,.,,,,,,,,,,,,,.*
                         .,,.@,,,,.,,         %%                 @,,,.,(.,,,..,,,,,,,,,,,,,,,,,,.///&(
                        ,,,%,,,,,,.,,  ,  ,  %%&//                &,,.,,,,.@.,/,,,,,&.,,,,,,,.@&&&////
                       .,#.,,,,,,,#,,	,, ,, &,,&/               #/(*,,,,,,@,,.%,,,&.,,,,..#&&&///////
                     /..#,.,,,.,,.,,,     /  ####%%               ,.,,,.,,&.,,,../,..,,%&&&///////@(((&
           ,%&%,@/( &,,.,,,,,,,&#,,,(     /%%####%%               @.((,,,,.,,,,,,(,,,&#/////////////#%
       (&#/////////(*,,,,,,,,,,.,,,,@       ,#*%%/           @@,  .,,,,,,,,%.%//#.,./%//////////(&((&
          .%//////&,,,,,,,,,,,,.,,,,*       #,#%               /  %..,,,,,,,%,%(&/////%///////////////%(
         (////////,,,,,.,,,,,,,,/,,,#       # #               /%% *(,,.,,,,,,*.%/////#///////////////#((@@
           #//////////&((&.,,,,#,,,,*       # %           ,,,*%%  %..,,,,,,,%,%(&/////%///////////////%($$**
        ///////##////(//@%//##&(%(((*       ***(( *@@@@@@@@@@     #%**#.,,,,.,./#/////////##////(//@%//##&(%(((*
        .///////////#(((((((*/,,/(&&,@*,*****,,*****************.,,,.%((((((((##////////////@/&#(&&%%%#((*&
       /(( /////////&(((((@&&.....(,.&##(********************&.,,,,.,,/((((&%@/((//@////&#(((##(((@#(((((
          @%.  (/, #&&%%&            ,,,//(((/*******%###%#/.      *,#(%,  ((/@((/#(%#(#((((((#(@((#((@((
                &.                                                        .* (& &@  #%  &@

		""")

	text = ' You find a child to your side \n You rembember to yourself when was child'
	print(text.upper())

	print(signStart, "You decide to be quiet")
	print(signStart, "you put out the matchstick")

	print("\n")
	sec1_1 = input(" ",)

	if sec1_1 == "1":
		call("clear")


		print("")
		print(COLOR_BANNER3, """


		██╗  ██╗██╗    ████████╗██████╗ ███████╗██╗  ██╗      ██████╗ ██████╗ ██████╗ ███████╗███████╗
		██║  ██║██║    ╚══██╔══╝██╔══██╗██╔════╝╚██╗██╔╝     ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
		███████║██║       ██║   ██████╔╝█████╗   ╚███╔╝█████╗██║     ██║   ██║██║  ██║█████╗  ███████╗
		██╔══██║██║       ██║   ██╔══██╗██╔══╝   ██╔██╗╚════╝██║     ██║   ██║██║  ██║██╔══╝  ╚════██║
		██║  ██║██║       ██║   ██║  ██║███████╗██╔╝ ██╗     ╚██████╗╚██████╔╝██████╔╝███████╗███████║
		╚═╝  ╚═╝╚═╝       ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝



			XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
			XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
			XX                                                                          XX
			XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
			XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
			XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
			XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
			XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
			XX   MMMMMy''                                                    ''yMMMMM   XX
			XX   MMMy'                                                          'yMMM   XX
			XX   Mh'                                                              'hM   XX
			XX   -                                                                  -   XX
			XX                                                                          XX
			XX   ::                                                                ::   XX
			XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
			XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
			XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
			XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
			XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
			XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
			XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
			XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
			XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
			XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
			XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
			XX                                oo      oo                                XX
			XX           oM                 oo          oo                 Mo           XX
			XX         oMMo                M              M                oMMo         XX
			XX       +MMMM                 s              s                 MMMM+       XX
			XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
			XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
			XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
			XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
			XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
			XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
			XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
			XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
			XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
			XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
			XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
			XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
			XX   MMMMMMMM-                                                  -MMMMMMMM   XX
			XX   MMMMMMMMM                                                  MMMMMMMMM   XX
			XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
			XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
			XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
			XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
			XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
			XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
			XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
			XX                                                                          XX
			XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
			XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
			
			    .o88o.                               o8o                .
			    888 `"                               `"'              .o8
			   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
			    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
			    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
			    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
			   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'			
				
			""", COLOR_BANNER_END)

		# ------- DEMAS CODIGO ACERCA DE COMO DESCOFICIAR EL ARCHIVO O UNIDAD  ------- 










