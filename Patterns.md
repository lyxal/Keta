# Different Block Patterns
This is a list of how patterns are evaluated within Ket (ekg).

Nilads: N n Ñ --> Nilads

Singles: S s Š  --> Monads

Infixes: I i Ī --> Dyads

L L* L& --> Left argument -- implicit/whatever is to the left

R R* R& --> Right argument -- implicit/whatever is to the left

`{...}` means that the expressions are blocked together

- `ND` -> `N I R`

- `SN` -> `S(N)`
- `Ss` -> `S(s(R))`
- `SI` -> `S(R) I R*`

- `IN` -> `L I S`
- `IS` -> `L I S(R*)`
- `Ii` -> `{L I R} i R*`

- `SNI` -> `S(N) I R`
- `SsN` -> `S(s(N))`
- `SsŠ` -> `S(s(Š(R)))`
- `SsI` -> `S(s(R)) I R*`
- `SIN` -> `S(R) I N`
- `SIs` -> `S(R) I s(R*)`
- `SIi` -> `S(R) I {L* i R*}`

- `INi` -> `{L I N} i R*`
- `ISN` -> `L I S(N)`
- `ISs` -> `L I S(s(R*))`
- `ISi` -> `{L D S(R*)} i R&`
- `IiN` -> `{L I R} i N`
- `IiS` -> `{L I R} i S(R*)`
- `IiĪ` -> `{{L I R} i R*} Ī R&`

Blocks are evaluated using the triplet rules if possible, otherwise the pair rules are used, otherwise expressions are evaluated as is.


