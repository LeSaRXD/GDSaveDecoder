# CCLocalLevels.xml tags:

## required tags

### level info:
- kCEK = 4 *always*

- k2 = name
- k3 = description (base64)
- k4 = level data (base64 -> gzip)

- k5 = Player *always* - makes the level appear

### unknown:
- k21 = 2 *always*

- k50 = 35 *always* - makes the game not decode level description and data from b64

## not required tags:

### stats:
- k14 = verified

- k18 = attempts

- k19 = best

- k20 = best practice

- k36 = jumps

- k45 = song id

- k48 = object count

## unknown:
- k13
- k16

- k34 = random string coded in b64 and gzip

- k47
- k48

- k67 = long string of repeating 0_ - appears after verifying

- k71
- k80
- k85
- k86
- k88
- k89
- k90

- kI1
- kI2
- kI3
- kI4
- kI5
- kI6



# Level header tags
> none of these are required for the level to open

- kS38 = all [colors](#color), seperator is |

- kA2 = gamemode (0-6)
- kA3 = is mini (0/1)
- kA4 = speed (0 - 1x, 1 - 0.5x, 2 - 2x, 3 - 3x, 4 - 4x)
- kA6 = ground id (starts from 1)
- kA7 = background id (starts from 1)
- kA8 = is dual (0/1)
- kA10 = 2-player mode
- kA17 = ground line type (1 - fading, 2 - solid)
- kA18 = font (0-11)

- kS39 = unknown

- kA9 = editor colors and song break, keep at 0
- kA13, kA14, kA15 = 0 or 1 *always* - crashes the game if not 0 or 1
- kA16 = unknown

# Color
- 1 = red component
- 2 = green component
- 3 = blue component
- 4 = copy player color (-1/0 - none, 1 - player color 1, 2 - player color 2)
- 5 = blending
- 6 = [color id](#color-ids)
- 7 = opacity
- 8 = 1
- 9 = copied color id
- 10 = copied color HSV `{hue}a{saturation}a{value}a{saturation is additive}a{value is additive}`
- 17 = use copied color opacity (0/1)
- 18 = 0

# Color IDs:
- 1000 = bg
- 1001 = g1
- 1009 = g2
- 1002 = line
- 1003 = 3D line
- 1004 = obj
- 1005 = p1
- 1006 = p2
