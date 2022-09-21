# CCLocalLevels.xml tags:

### required:

    kCEK = 4 (always)

    k2 = name
    k3 = description (base64)
    k4 = level data (base64 > gzip)

    k5 = Player (always) - makes the level appear

    k21 = 2 (always)

    k50 = 35 (always) - makes the game not decode level description and data from b64



### stats - not required:

    k14 = <t /> only if verified

    k18 = attempts

    k19 = best - affects in-game value when changed

    k20 = best practice

    k36 = jumps

    k48 = object count

### unknown:

    k34 = random string coded in b64 and gzip

    k16, k85, k86 - random <t />

    k13 = <t />
    k47 = <t />
    k89 = <t />

    k80

    k85
    k86

    k67 = long string of repeating 0_ - appears after verifying



### removed successfully:

    reappeared:

        k47 - after opening the editor
        k48 - after opening the editor

        k80

        kI1
        kI2
        kI3
        kI6

    didn't reappear:

        k14 - for verification

        k16

        k13
        k89

        k34

        k71
        k90

        k85
        k86

        k88

        k67

        kI4
        kI5

### removed unsuccessfully:

    k21 - level became unviewable and looked like it was uploaded
    k50 - level description and level arent decrypted using b64



# Level data tags

kS38 = all colors, seperator is |
color:
    1 = red component
    2 = green component
    3 = blue component
    6 = color id (
        1000 = bg,
        1001 = g1,
        1009 = g2,
        1002 = line,
        1004 = obj,
        1005 = p1,
        1006 = p2
    )

kA2 = gamemode (0-6)
kA3 = is mini (0/1)
kA4 = speed (0 - normal, 1 - slow, 2 - 2x, 3 - 3x, 4 - 4x)
kA8 = is dual (0/1)
kA9 = editor colors and song break, keep at 0
kA18 = font (0-11)



kS39 = unknown

kA6 = unknown
kA7 = unknown

kA13 = unknown
kA14 = unknown
kA15 = unknown
kA16 = unknown
kA17 = unknown