# food-picture v1: pepperoni pizza cheese pull

## The entry

A hand lifts a slice of pepperoni pizza and the mozzarella stretches in
one long, glossy pull back toward the pie. The crust is blistered from
the oven, the pepperoni edges are crisped, and oven fire glows in the
background. It is a single food photograph, made to look delicious at
first glance.

## Why it fits the rubric

- **Appetite appeal:** the cheese pull is the first thing the eye lands
  on, and melted cheese mid-stretch reads as hot and ready to eat.
- **Fresh and real:** the pizza looks freshly baked, not staged — blistered
  crust, shining cheese, curled pepperoni, warm oven light.
- **Texture you can feel:** gloss on the cheese, crunch on the crust,
  grease sheen on the pepperoni, heat in the background.
- **Styling and light:** warm oven glow against a darker background keeps
  the slice as the clear subject; nothing competes with it.
- **Clean craft:** one clean photograph, no text, no borders, no artifacts.
- **Readable small:** the slice and the cheese pull stay obvious even
  shrunk down to a thumbnail.

## How to run

```bash
python3 main.py
```

The program reads the embedded base64 image, decodes it, and writes
`entry.png` into the directory given by `MAKEFUN_OUTPUT_DIR`
(default `/output`). It needs no arguments and no extra files — the
image travels inside `main.py` itself.

## Determinism

The output is byte-identical on every run: the same embedded bytes are
decoded and written each time, with no timestamps, randomness, or
network access. The program uses only the Python standard library.

## License

MIT — see `LICENSE`.
