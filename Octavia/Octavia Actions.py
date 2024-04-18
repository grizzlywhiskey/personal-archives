- name: Smoke Stick
  automation:
    - type: text
      text: As an action, you can ignite a smokestick using a torch, tinderbox, or
        other source of fire or intense heat. Once ignited, the smokestick is
        consumed and a 10-foot cube around it is filled with smoke for one
        minute. This area is heavily obscured. A moderate or strong wind
        disperses the smoke in one round.
      title: Effect
    - type: counter
      counter: Smoke Stick
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
    - type: target
      target: self
      effects:
        - type: ieffect2
          name: Smoke Stick
          duration: "10"
          effects: null
          attacks: []
          buttons: []
          end: true
          conc: false
          desc: Heavily obscured by smoke
          stacking: false
          save_as: null
          parent: null
          target_self: false
          tick_on_caster: false
  _v: 2
  verb: deploys
  thumb: https://media.giphy.com/media/5ts7ZMa1hiThWHmFSP/giphy.gif
  activation_type: 1
- name: Smoke Pellet
  automation:
    - type: text
      text: As an action or bonus action, you can throw a smoke pellet at a point
        within 10 feet or you. The smoke pellet then detonates, creating a
        10-foot cube filled with smoke. This area is heavily obscured until the
        end of your next turn.
      title: Effect
    - type: counter
      counter: Smoke Pellet
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
    - type: target
      target: self
      effects:
        - type: ieffect2
          name: Smoke Pellet
          duration: "1"
          effects: null
          attacks: []
          buttons: []
          end: true
          conc: false
          desc: Heavily obscured by smoke
          stacking: false
          save_as: null
          parent: null
          target_self: false
          tick_on_caster: false
  _v: 2
  verb: deploys
  thumb: https://media.giphy.com/media/LIWK8pYTowUsmny2Bz/giphy.gif
  activation_type: 3
- name: Soul Ring
  automation:
    - type: text
      text: >-
        This ring contains a small, deep black stone forged from collected Soul
        Stones.

        As an action the wearer can release the trapped soul energy, black smoke rises from the ring and is inhaled by a creature within 5ft. A creature that inhales the black smoke has their soul tethered to the wearer for 1 minute, during which time the wearer knows their whereabouts, and adds 1d4 to persuasion checks against them. Once the ring has been used in this way, it cannot be used again until the next dawn.  Constructs, or creatures that do not need to breathe are immune to this feature.


        __*This is a special memento of the 2022 Soul Tower Halloween Event, and cannot be traded, purchased, or crafted.*__
      title: Effect
    - type: counter
      counter: Soul Ring
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
    - type: target
      target: self
      effects: []
  _v: 2
  proper: true
  verb: activates their
  phrase: '"All that holds back the voice of many, so they are never heard.
    Spirits of muting, frustration, and fear of speaking torment in this place,
    I release thee."'
  thumb: https://images-ext-1.discordapp.net/external/EqciyINk7NBcmyxwNwn4cu1kc0DRxfY3029-vRtHnCo/https/i.pinimg.com/564x/02/17/1b/02171bdb190aaaf602b3241ee4e0eca3.jpg
  activation_type: 1
- name: Anniversary Spear (Year 1)
  automation:
    - type: text
      text: >-
        This gilded spear is made from dense, black metal.  At the base of the
        spear sits a heavily weighted "1" that has been hand forged into the
        metal of the weapon.  Balancing this out, the tip of the spear is larger
        than usual, and glows a soft golden light.   As a bonus action, the
        spear can be activated and small harmless radiant gold sparks shoot
        forth from the spears tip, if one were to listen carefully, they could
        hear the cheers of all the souls lost at the hand of Strand.


        *__This item is a unique memento of the 2022 Enter Ravenloft 1st Birthday.  It cannot be crafted, traded, or sold.__*
      title: Effect
  _v: 2
  proper: true
  verb: creates golden flourishes with their
  thumb: https://media.discordapp.net/attachments/933501504059473951/1035641840440979456/1-year-spear.png
  activation_type: 8
- name: Shove (Prone)
  automation:
    - type: target
      target: 1
      effects:
        - type: check
          ability:
            - acrobatics
            - athletics
          contestAbility:
            - athletics
          fail:
            - type: ieffect2
              name: Prone
              duration: null
              effects:
                attack_advantage: "-1"
              attacks: []
              buttons:
                - label: Stand Up
                  automation:
                    - type: remove_ieffect
                  verb: stands up
                  style: "3"
                  defaultDC: null
                  defaultAttackBonus: null
                  defaultCastingMod: null
              end: false
              conc: false
              desc: A prone creature's only movement option is to crawl, unless it stands up
                and thereby ends the condition.
              stacking: false
              save_as: null
              parent: null
              target_self: false
              tick_on_caster: false
          contestTie: neither
    - type: text
      text: >-
        Using the Attack action, you can make a special melee attack to shove a
        creature, either to knock it prone or push it away from you. If you’re
        able to make multiple attacks with the Attack action, this attack
        replaces one of them.


        The target must be no more than one size larger than you and must be within your reach. Instead of making an attack roll, you make a Strength (Athletics) check contested by the target’s Strength (Athletics) or Dexterity (Acrobatics) check (the target chooses the ability to use). You succeed automatically if the target is incapacitated. If you succeed, you either knock the target prone or push it 5 feet away from you.
      title: Effect
  _v: 2
  proper: true
  verb: attempts to
  activation_type: 1
- name: Relentless
  automation:
    - type: target
      target: self
      effects:
        - type: damage
          damage: -1 [healing]
          overheal: false
    - type: text
      text: When you are reduced to 0 hit points but not killed outright, you can drop
        to 1 hit point instead. You can’t use this feature again until you
        finish a long rest.
      title: Effect
    - type: counter
      counter: Relentless
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
  _v: 2
  proper: true
  verb: is
  thumb: https://i.pinimg.com/564x/91/aa/d9/91aad91f65a6c5d434e99049de880a97.jpg
  activation_type: 8
- name: Merge with Shadow
  automation:
    - type: text
      text: You can cast the pass without trace spell once with this trait and you
        regain the ability to do so when you finish a long rest. You can also
        cast this spell using any spell slots you have.
      title: Effect
    - type: spell
      id: 2201
      level: null
      dc: null
      attackBonus: null
      castingMod: null
      parent: null
    - type: counter
      counter: "Merge with Shadow (4): Pass without Trace"
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
  _v: 2
  proper: true
  verb: helps the party
  activation_type: 1
- name: Circlet of Blasting
  automation:
    - type: spell
      id: 2238
      level: null
      dc: null
      attackBonus: "5"
      castingMod: null
      parent: null
    - type: counter
      counter: Circlet of Blasting
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
  _v: 2
  proper: true
  verb: activates her
- name: Earring of Message
  automation:
    - type: text
      text: The blue crystal of this earring is wrapped with delicate copper wire. The
        earring has 5 charges. While wearing it, you can use an action to expend
        1 charge and cast the message spell. The earring regains 1d4 + 1
        expended charges daily at dawn.
      title: Effect
    - type: spell
      id: 2188
      level: null
      dc: null
      attackBonus: null
      castingMod: null
      parent: null
    - type: counter
      counter: Earring of Message
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
  _v: 2
  proper: true
  verb: activates their
  thumb: https://images-ext-1.discordapp.net/external/eGe9ie-8d9mFtut2fG3cW-rTFMrak8q4KLQpY3NfnYs/https/media-waterdeep.cursecdn.com/avatars/thumbnails/24407/170/315/315/637828636930896127.jpeg
  activation_type: 1
- name: Pipes of Haunting
  automation:
    - type: text
      text: You can use an action to play them and expend 1 charge to create an eerie,
        spellbinding tune. Each creature you choose within 30 feet of you that
        hears you play must succeed on a DC 15 Wisdom saving throw or become
        frightened of you for 1 minute.  A creature that succeeds its saving
        throw is immune to the effect of these pipes for 24 hours.   A creature
        that fails the saving throw can repeat it at the end of each of its
        turns, ending the effect on itself on a success.
      title: Effect
    - type: target
      target: each
      effects:
        - type: save
          stat: wis
          fail:
            - type: ieffect
              name: Frightened of Octavia
              duration: "10"
              effects: ""
              end: false
              conc: false
              desc: null
              stacking: false
              save_as: null
              parent: null
          success: []
          dc: "15"
    - type: counter
      counter: Pipes of Haunting
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
  _v: 2
  proper: true
  verb: plays her
  phrase: A tree ascended there. Oh pure transendence! Oh Orpheus sings! Oh tall
    tree in the ear! And all things hushed. Yet even in that silence a new
    beginning, beckoning, change appeared.  Creatures of stillness crowded from
    the bright unbound forest, out of their lairs and nests; and it was not from
    any dullness, not from fear, that they were so quiet in themselves,  but
    from just listening. Bellow, roar, shriek seemed small inside their hearts.
    And where there had been at most a makeshift hut to receive the music,  a
    shelter nailed up out of their darkest longing, with an entryway that
    shuddered in the wind- you built a temple deep inside their hearing.
  thumb: https://i.pinimg.com/564x/81/76/8e/81768e49cf7bce599bd7affbfca62f38.jpg
  activation_type: 1
- name: NIght Caller
  automation:
    - type: spell
      id: 1996
      level: null
      dc: null
      attackBonus: null
      castingMod: null
      parent: null
    - type: text
      text: >-
        If you blow the whistle in darkness or under the night sky, it allows you
        to cast the animate dead spell. The target can be affected through up to
        10 feet of soft earth or similar material, and if it is, it takes 1
        minute to claw its way to the surface to serve you. Once the whistle has
        animated an undead creature, it can't do so again until 7 days have
        passed.


        Once every 24 hours, you can blow the whistle to reassert control over one or two creatures you animated with it.
      title: Effect
    - type: counter
      counter: Night Caller
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
  _v: 2
  proper: true
  verb: players her
  activation_type: 8
- name: "Spellwrought Tattoo : Shield"
  automation:
    - type: text
      text: This magic tattoo contains a single 1st Level Spell, wrought on your skin
        by a magic needle. To use the tattoo, you must hold the needle against
        your skin and speak the command word. The needle turns into ink that
        becomes the tattoo, which appears on the skin in whatever design you
        like. Once the tattoo is there, you can cast its spell, requiring no
        material components. The tattoo glows faintly while you cast the spell
        and for the spell's duration. Once the spell ends, the tattoo vanishes
        from your skin.
      title: Effect
    - type: counter
      counter: "Spellwrought Tattoo : Shield"
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
    - type: spell
      id: 2247
      level: null
      dc: null
      attackBonus: null
      castingMod: null
      parent: null
  _v: 2
  proper: true
  verb: activates her
  thumb: https://i.pinimg.com/564x/da/77/bd/da77bdeb143f41c9e4c8c721d0a1f9a6.jpg
  activation_type: 4
- name: "Spellwrought Tattoo : Bless"
  automation:
    - type: text
      text: This magic tattoo contains a single 1st Level Spell, wrought on your skin
        by a magic needle. To use the tattoo, you must hold the needle against
        your skin and speak the command word. The needle turns into ink that
        becomes the tattoo, which appears on the skin in whatever design you
        like. Once the tattoo is there, you can cast its spell, requiring no
        material components. The tattoo glows faintly while you cast the spell
        and for the spell's duration. Once the spell ends, the tattoo vanishes
        from your skin.
      title: Effect
    - type: counter
      counter: "Spellwrought Tattoo : Bless"
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
    - type: spell
      id: 2016
      level: null
      dc: null
      attackBonus: null
      castingMod: null
      parent: null
  _v: 2
  proper: true
  verb: activates her
  thumb: https://i.pinimg.com/564x/da/77/bd/da77bdeb143f41c9e4c8c721d0a1f9a6.jpg
  activation_type: 4
- name: Soul Cage
  automation:
    - type: counter
      counter: Soul Cage
      amount: "-6"
      allowOverflow: false
      errorBehaviour: raise
    - type: spell
      id: 14601
      level: null
      dc: null
      attackBonus: null
      castingMod: null
      parent: null
  _v: 2
  proper: true
  verb: generates
  thumb: https://media.discordapp.net/attachments/920796422922715136/1093337534504894595/motes.jpg
  activation_type: 4
- name: Steal Life (Soul Cage)
  automation:
    - type: text
      text: You can use a bonus action to drain vigor from the soul and regain 2d8 hit
        points.
      title: Steal Life
    - type: counter
      counter: Soul Cage
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
    - type: target
      target: self
      effects:
        - type: damage
          damage: -2d8 [healing]
          overheal: false
  _v: 2
  proper: true
  verb: channels
  activation_type: 3
- name: Query Soul (Soul Cage)
  automation:
    - type: text
      text: You ask the soul a question (no action required) and receive a brief
        telepathic answer, which you can understand regardless of the language
        used. The soul knows only what it knew in life, but it must answer you
        truthfully and to the best of its ability. The answer is no more than a
        sentence or two and might be cryptic.
      title: Query Soul
    - type: counter
      counter: Soul Cage
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
  _v: 2
  proper: true
  verb: proceeds to
  activation_type: 2
- name: Eyes of the Dead (Soul Cage)
  automation:
    - type: text
      text: >-
        You can use an action to name a place the humanoid saw in life, which
        creates an invisible sensor somewhere in that place if it is on the
        plane of existence you're currently on. The sensor remains for as long
        as you concentrate, up to 10 minutes (as if you were concentrating on a
        spell). You receive visual and auditory information from the sensor as
        if you were in its space using your senses.


        A creature that can see the sensor (such as one using see invisibility or truesight) sees a translucent image of the tormented humanoid whose soul you caged.
      title: Query Soul
    - type: counter
      counter: Soul Cage
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
  _v: 2
  proper: true
  verb: proceeds to
  activation_type: 1
- name: Feather Token
  automation:
    - type: text
      text: >-
        This small metal disk is inscribed with the image of a feather. When you
        fall at least 20 feet while the token is on your person, you descend 60
        feet per round and take no damage from falling. The token's magic is
        expended after you land, whereupon the disk becomes nonmagical.


        *If you buy another feather token - feather fall, add +1 to the custom counter!*
      title: Feather Token
    - type: spell
      id: 2095
      level: null
      dc: null
      attackBonus: null
      castingMod: null
      parent: null
    - type: counter
      counter: Feather Token
      amount: "1"
      allowOverflow: false
      errorBehaviour: warn
  _v: 2
  proper: true
  verb: activates her
  thumb: https://i.pinimg.com/564x/52/6b/76/526b7630acd37dc5def8f30ba1e4b73c.jpg
  activation_type: 4
