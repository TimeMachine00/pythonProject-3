
print("created by hussainatphysics@gmail.com(hussainsha syed)")

"""
we are creating Tressure finding game....

"""

print("Welcome to BABYLON TRESSURE finding.")
print("Here mission is to find the Diomonds.")

print("""
                         

                               HHHHHHHHHHHHHH
                           $HHHHHH$$$$$$$HHHHHHH
                        HHHHHHHH$$H$$$$$::$$HHHHHH$$
                      HHHHHHHHHHHHHHHHH$$::$$$HHHHH$H$
                   HHHHHHHHHHHHH$HHHHHHHHH$$$$$$HHH$$:$$
                 $HHHH$HHHHHHHHH$$HHHHH$$$HH$$H$$H$$::$H$$
               $HHHH$HHHHHH^^     ^HH^    :HH$HH$$$::$HH$$$
              HHHH$$HHHHH^:                :h$$HH$$$$HHH$H$$
             HHHH$$HHHH^::                  ;$$hHHH$HHHHH$ $
            $HHH$:HHHHH::                   $$ H$H$$H$H$$HHHH$
            $HH$:HHHHHH:::                  H:  $$HHHH$$HHHHh $
            HHH$:$HHHHH::                   H$ ..$$HHHHHHH$$$$H
           $HHHH$$$$HHH$$:::...        ...:$$HH$HH$HHHH$HH$$HH$H
          $HHHHH$HHHHH$:.._.'''':     ````_.._..H^HH$$HHHHHH$$ H
          HHHH$$HHHHHH::=<_(@)~>:\    . /~(@)_>= :HHHH$$$$$HHH$$
         $H$$$::$$HHHH:: ''~~~~~ :`     ~~~~~``  ::H$$HHH$$$$HH$
        $H$HHH$$$HHHHH:          ::  '           : HH::$HHHHHHH $
        HH$HHHH$$$HHHH$          :|  :           :HH$H$::$HHHHH$$
         H$$$HHHHHHHHH$         :/|  :\         ::HHHHHHH$$$$HHHH$
        $$HH$HHHHHHHHH$$       :(:.__.:)  .    :::HH$$$HHHH$:::$$$$
       $$HH$HHH$HHHHHH$$:  .:'             `. '  :HHH$$:::$$HH$$HH$$
      $$HHHHHH$$H$HHHH$$:  : . _..-..-.._ . '    :HHHH$$::$$H$H$$H$H
      $HHHH$$::HHHHHHHH$::    ~=--------=~      .$H$HHHHHHHHH$$:HH$
       H$$$::HHHHHHHHHH$$:.     ~------~       .$HHHHH$$HHHH$$::H$
     $H$$$HHHHHH$$HHHHHHH$::..              ..$HHHHHHHHHHHH$$:$$$$H
    $H$$HH$$$$HHH$$HHHHHHHH$$::          .:$HHHHHHHHHHHHHH$$$$$HHH$
     H$$$HHHH$$HHHH$HHHHHHHHHHHn.__..__.nHHHH$HHHHH%%%HHHHHH$$$HHH
    $HHDrSHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH$HHHHH%%%%%%%%HHHHHH$HH$
   $HHHHHH$HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH$H$HH%%%%%%%%%%%%%HHHHHHH
    $HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH$$$H%%%%%%%%%%%%%%%%%HHHHHH




""")

path= input("which path will you choose? Left or Right?\n")

path = path.lower()

if path == "left":
  print("game over baby, you are a mean for evil")
elif path == "right":
  swim= input("would you like swim or wait? \n")
  swim=swim.lower()

  if swim == 'swim':
    print("game over now you are a dinner for sea evil")
  elif swim=='wait':
    room= input("which door you want to pick? red, blue, green?\n")
    room=room.lower()

    if room=='green':
      print("game over you will become evil now for ever")
    elif room =='blue':
      print("game over you will be an evil for some days")
    elif room == 'red':
      print("ureka!!!!!!!!you WON the Game, Here are your Diomands")
else:

  print("game over")


# Just for exe file
print()
print(input("press enter for byeeeeeeeeeee"))