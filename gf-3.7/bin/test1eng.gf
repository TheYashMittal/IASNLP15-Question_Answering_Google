concrete test1eng of test1 = {
	lincat
		Person_generic, Person_specific, Mod, Statement, Action, Kartaa, Karma = { s : Str } ;
	lin
		Create_statement Action Kartaa Karma = { s = Kartaa.s ++ Action.s ++  Karma.s } ;
                Create_spec Person1 = { s = "the" | "a" ++ Person1.s } ;
                Create_mod Mod Person1 = { s = Mod.s ++ Person1.s } ;
                Create_kartaa Person1 = { s = Person1.s } ;
                Create_karma Person1 = { s = Person1.s } ;
                saw = { s = "saw" } ;
                Ram = { s = "Ram" } ;
                Mary = { s = "Mary" } ;
                Girl = { s = "girl" } ;
                beautiful = { s = "beautiful" } ;
}