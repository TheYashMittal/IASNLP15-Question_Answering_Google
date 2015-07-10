abstract test2 = {
	cat
		Person_generic ; Person_specific ; Mod ; Statement ; Action ; Kartaa ; Karma ; Thing_generic ; Thing_specific ;
	flags startcat = Statement ;
	fun
		Create_statement : Action -> Kartaa -> Karma -> Statement ;
		Create_spec1 : Person_generic -> Person_specific ;
		Create_spec2 : Thing_generic -> Thing_specific ;
		Create_mod1 : Mod -> Person_generic -> Person_generic ;
		Create_mod2 : Mod -> Thing_generic -> Thing_generic ;
		Create_kartaa : Person_specific -> Kartaa ;
		Create_karma : Thing_specific -> Karma ;
		cut : Action ;
		fruit : Thing_generic ;
		Ram : Person_specific ;
}
