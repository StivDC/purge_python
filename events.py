#events
Kirill_van = {
	"ascii":
	"""
        _______________________
       |                       |
       |  ~ KIRILL VAN ~    ___|
       |                    |----.
       |  "HERE TO HELP!"   | |O,|____
       |  .-.               | -  .-.  |
  `@@ =(_| @ |______________|___| @ |_) 
          `-'                    `-'
	""",

	"id": "Kirill_van",

	"name": "Kirill's magical healing van",

	"description": """Kirill finds you in his magical van!
He asks you for your student ID,
if you have it he says you shall be granted an item.
If not he shall leave in a haste.
You may not be given this opportunity again.
	"""
}
Crazy_gang = {
	"ascii":
	"""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMds+:--------:+sdNMMMMMMMMMMM
MMMMMMMMms:-+sdNMMMMMMMMNdy+--omMMMMMMMM
MMMMMMh:` /mMMMMMMMMMMMMMMMMm+ `-yMMMMMM
MMMMd--hN``--sNMMMMMMMMMMNy:..`md:.hMMMM
MMM+`yMMMy hd+./hMMMMMMh/.+dd sMMMh`/MMM
MM:.mMMMMM:.NMMh/.+dd+./hMMM--MMMMMm--NM
M+`mMMMMMMN`+MMMMm-  .dMMMMo mMMMMMMN.:M
d yMMMMMMMMy dNy:.omNs--sNm oMMMMMMMMh h
/`MMMMMMMMMM.`.+dMMMMMMm+.``NMMMMMMMMM-:
.:MMMMMMMd+./`oMMMMMMMMMMs /.+dMMMMMMM/`
.:MMMMmo.:yNMs dMMMMMMMMm`oMNy:.omMMMM/`
/`MNy:.omMMMMM--MMMMMMMM:.MMMMMNs--sNM.:
d -` :++++++++: /++++++/ :++++++++:  : h
M+ yddddddddddd+ yddddy /dddddddddddy`/M
MM/.mMMMMMMMMMMM.-MMMM/.NMMMMMMMMMMm.:NM
MMMo`sMMMMMMMMMMd sMMy hMMMMMMMMMMy`+MMM
MMMMd--hMMMMMMMMM+`mN`/MMMMMMMMMh--hMMMM
MMMMMMh:.omMMMMMMN.:/`NMMMMMMms.:hMMMMMM
MMMMMMMMNs:./shmMMh  yMMNds/.:smMMMMMMMM
MMMMMMMMMMMMdy+/---``---:+sdMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

	""",

	"id": "Crazy_gang",

	"name": "A crazy gang",

	"description": """You encounter a crazy gang!
They have a strange logo on their arm.
You can either fight, flee or bribe.
If you bribe without enough money, you will die.
They take a bribe of £50.
Fighting could be costly.
	"""
}
Machete_murderer = {
	"ascii":
	"""                       ____________
                      .~      ,   . ~.
                     /                \
                    /      /~\/~\   ,  \
                   |   .   \    /   '   |
                   |         \/         |
          XX       |  /~~\        /~~\  |       XX
        XX  X      | |  o  \    /  o  | |      X  XX
      XX     X     |  \____/    \____/  |     X     XX
 XXXXX     XX      \         /\        ,/      XX     XXXXX
X        XX%;;@      \      /  \     ,/      @%%;XX        X
X       X  @%%;;@     |           '  |     @%%;;@  X       X
X      X     @%%;;@   |. ` ; ; ; ;  ,|   @%%;;@     X      X
 X    X        @%%;;@                  @%%;;@        X    X
  X   X          @%%;;@              @%%;;@          X   X
   X  X            @%%;;@          @%%;;@            X  X
    XX X             @%%;;@      @%%;;@             X XX
      XXX              @%%;;@  @%%;;@              XXX
                         @%%;;%%;;@
                           @%%;;@
                         @%%;;@..@@""",
  
	"id": "Machete_murderer",

	"name": "A dual weilding machete murderer",

	"description": """You encounter a dual weilding machete murderer.
It seems impossible to bribe him.
He seems impossible to defeat.
This might be your demise.
	"""
}
Sneak_attack = {
	"ascii": 
	"""
	              | |____________________________________________________
 _ _ _ _ _ _ _| |                                                  .'`.
|_|_|_|_|_|_|_| |------------------------------------------------.'****>
`.            | |_______________________________________________.'***.'
  `.        .'| |                                               `**'
    `-.___.'  `-'                                              .'*`.
                                                               `._.' .
                                                               .   .'*`.
                                                             .'*`. `._.'
	""",
	"id": "Sneak_attack",

	"name": "A SNEAK ATTACK!",

	"description": """A SNEAK ATTACK!
You've been ganked!
Taking a massive amount of damage.
It seems like it could be fatal.
	"""
	#Left to bleed on the ground.
	#If no bandage applied within two turns bleed to death - function yet to implement.
}
Random_item = {
	"ascii":
	"""
	         ________
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####
                       d###P
                    _g###@F
                 _gN##@P
               gN###F"
              d###F
             0###F
             0###F
             0###F
             "NN@'

              ___
             q###r
              ""
	""",

	"id": "Random_item",

	"name": "An item on the ground",

	"description": """You see something on the ground,
the appearance of it seems like an item you could use or pocket.
You hope for the best as you reach down to pick it up.
	"""
}
game_events = {
	"1" : Kirill_van,
	"3": Crazy_gang,
	"5": Machete_murderer,
	"7": Sneak_attack,
	"9": Random_item
}
