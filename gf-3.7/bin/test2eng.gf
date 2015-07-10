concrete test2eng of test2 = {
	lincat
		Person_generic, Person_specific, Mod, Statement, Action, Kartaa, Karma, Thing_generic, Thing_specific = { s : Str } ;
	lin
		Create_statement Action Kartaa Karma = { s = Kartaa.s ++ Action.s ++  Karma.s } ;
                Create_spec1 Person1 = { s = "a" ++ Person1.s } ;
		Create_spec2 Thing1 = { s = "a" ++ Thing1.s } ;
                Create_mod1 Mod Person1 = { s = Mod.s ++ Person1.s } ;
		Create_mod2 Mod Thing1 = { s = Mod.s ++ Thing1.s } ;
                Create_kartaa Person1 = { s = Person1.s } ;
                Create_karma Thing1 = { s = Thing1.s } ;
                cut = { s = "cut" } ;
                Ram = { s = "Ram" } ;
                fruit = { s = "fruit" } ;
}

