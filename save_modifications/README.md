required:

    kCEK = 4 (always)

    k2 = name
    k3 = description (base64)
    k4 = level data (base64 > gzip)

    k5 = Player (always) - makes the level appear

    k21 = 2 (always)

    k50 = 35 (always) - makes the game not decode level description and data from b64



stats - not required:

    k14 = <t /> only if verified

    k18 = attempts

    k19 = best - affects in-game value when changed

    k20 = best practice

    k36 = jumps

    k48 = object count

unknown:

    k34 = random string coded in b64 and gzip

    k16, k85, k86 - random <t />

    k13 = <t />
    k47 = <t />
    k89 = <t />

    k80

    k85
    k86

    k67 = long string of repeating 0_ - appears after verifying



removed successfully:

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

removed unsuccessfully:

    k21 - level became unviewable and looked like it was uploaded
    k50 - level description and level arent decrypted using b64
