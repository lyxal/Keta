# Different Block Patterns
This is a list of how patterns are evaluated within Ket (ekg)

Nilads: N n Ñ ñ --> Nilads
Singles: S s Š ś --> Monads
Infixes: I i Ī ī --> Dyads

L L* L& L! --> Left argument -- implicit/whatever is to the left
R R* R& R! --> Right argument -- implicit/whatever is to the left

`{...}` means that the expressions are blocked together

`ND` -> `N I R`

`SN` -> `S(N)`
`Ss` -> `S(s(R))`
`SI` -> `S(R) I R*`

`IN` -> `L I S`
`IS` -> `L I S(R*)`
`Ii` -> `{L I R} i R*`

`SNs` -> `S(N)s(R)`
`SNI` -> `S(N) I R`
`SsN` -> `S(s(N))`
`SsŠ` -> `S(s(Š(R)))`
`SsI` -> `S(s(R)) I R*`
`SIN` -> `S(R) I N`
`SIs` -> `S(R) I s(R*)`
`SIi` -> `S(R) I {L* i R*}`

`INS` -> `L I N S(*R)`


