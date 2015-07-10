abstract d = {
        cat
                Person_generic ; Person_specific ; Mod ; Statement ; Action ; Kartaa ; Karma ;
        flags startcat = Statement ;
        fun
                Create_statement : Action -> Kartaa -> Karma -> Statement ;
                Create_spec : Person_generic -> Person_specific ;
                Create_mod : Mod -> Person_generic -> Person_generic ;
                Create_kartaa : Person_specific -> Kartaa ;
                Create_karma : Person_specific -> Karma ;
                saw : Action ;
                Ram : Person_specific ;
                Girl : Person_generic ;
                Mary : Person_specific ;
                Good : Mod ;
}