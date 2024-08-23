import random

def desc():
    return "Word Stuffing Entropy Reduction"

def create_words_string(words, words_num):
    words_list = words.split()
    return ', '.join(f'"{random.choice(words_list)}"' for _ in range(int(words_num)))


def run():
    words_num = 12000 

    words = '''
A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then, take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place.
- from Manual of Muad'Dib by the Princess Irulan
In the week before their departure to Arrakis, when all the final scurrying about had reached a nearly unbearable frenzy, an old crone came to visit the mother of the boy, Paul.
It was a warm night at Castle Caladan, and the ancient pile of stone that had served the Atreides family as home for twenty-six generations bore that cooled-sweat feeling it acquired before a change in the weather.
The old woman was let in by the side door down the vaulted passage by Paul's room and she was allowed a moment to peer in at him where he lay in his bed.
By the half-light of a suspensor lamp, dimmed and hanging near the floor, the awakened boy could see a bulky female shape at his door, standing one step ahead of his mother. The old woman was a witch shadow - hair like matted spiderwebs, hooded 'round darkness of features, eyes like glittering jewels.
Is he not small for his age, Jessica? the old woman asked. Her voice wheezed and twanged like an untuned baliset.
Paul's mother answered in her soft contralto: The Atreides are known to start late getting their growth, Your Reverence.
So I've heard, so I've heard, wheezed the old woman. Yet he's already fifteen.
Yes, Your Reverence.
He's awake and listening to us, said the old woman. Sly little rascal. She chuckled. But royalty has need of slyness. And if he's really the Kwisatz Haderach . . . well . . .
Within the shadows of his bed, Paul held his eyes open to mere slits. Two bird-bright ovals - the eyes of the old woman - seemed to expand and glow as they stared into his.
Sleep well, you sly little rascal, said the old woman. Tomorrow you'll need all your faculties to meet my gom jabbar.
And she was gone, pushing his mother out, closing the door with a solid thump.
Paul lay awake wondering: What's a gom jabbar?
In all the upset during this time of change, the old woman was the strangest thing he had seen.
Your Reverence .
And the way she called his mother Jessica like a common serving wench instead of what she was - a Bene Gesserit Lady, a duke's concubine and mother of the ducal heir.
Is a gom jabbar something of Arrakis I must know before we go there? he wondered.
He mouthed her strange words: Gom jabbar . . . Kwisatz Haderach .
There had been so many things to learn. Arrakis would be a place so different from Caladan that Paul's mind whirled with the new knowledge. Arrakis - Dune - Desert Planet .
Thufir Hawat, his father's Master of Assassins, had explained it: their mortal enemies, the Harkonnens, had been on Arrakis eighty years, holding the planet in quasi-fief under a CHOAM Company contract to mine the geriatric spice, melange. Now the Harkonnens were leaving to be replaced by the House of Atreides in fief-complete - an apparent victory for the Duke Leto. Yet, Hawat had said, this appearance contained the deadliest peril, for the Duke Leto was popular among the Great Houses of the Landsraad.
A popular man arouses the jealousy of the powerful, Hawat had said.
Arrakis - Dune - Desert Planet .
Paul fell asleep to dream of an Arrakeen cavern, silent people all around him moving in the dim light of glowglobes. It was solemn there and like a cathedral as he listened to a faint sound - the drip-drip-drip of water. Even while he remained in the dream, Paul knew he would remember it upon awakening. He always remembered the dreams that were predictions.
The dream faded.
Paul awoke to feel himself in the warmth of his bed - thinking . . . thinking. This world of Castle Caladan, without play or companions his own age, perhaps did not deserve sadness in farewell. Dr. Yueh, his teacher, had hinted that the faufreluches class system was not rigidly guarded on Arrakis. The planet sheltered people who lived at the desert edge without caid or bashar to command them: will-o'-the-sand people called Fremen, marked down on no census of the Imperial Regate.
Arrakis - Dune - Desert Planet .
Paul sensed his own tensions, decided to practice one of the mind-body lessons his mother had taught him. Three quick breaths triggered the responses: he fell into the floating awareness . . . focusing the consciousness . . . aortal dilation . . . avoiding the unfocused mechanism of consciousness . . . to be conscious by choice . . . blood enriched and swift-flooding the overload regions . . . one does not obtain food-safety-freedom by instinct alone . . . animal consciousness does not extend beyond the given moment nor into the idea that its victims may become extinct . . . the animal destroys and does not produce . . . animal pleasures remain close to sensation levels and avoid the perceptual . . . the human requires a background grid through which to see his universe . . . focused consciousness by choice, this forms your grid . . . bodily integrity follows nerve-blood flow according to the deepest awareness of cell needs . . . all things/cells/beings are impermanent . . . strive for flow-permanence within . . .
Over and over and over within Paul's floating awareness the lesson rolled.
When dawn touched Paul's window sill with yellow light, he sensed it through closed eyelids, opened them, hearing then the renewed bustle and hurry in the castle, seeing the familiar patterned beams of his bedroom ceiling.
The hall door opened and his mother peered in, hair like shaded bronze held with a black ribbon at the crown, her oval face emotionless and green eyes staring solemnly.
You're awake, she said. Did you sleep well?
Yes.
He studied the tallness of her, saw the hint of tension in her shoulders as she chose clothing for him from the closet racks. Another might have missed the tension, but she had trained him in the Bene Gesserit Way - in the minutiae of observation. She turned, holding a semiformal jacket for him. It carried the red Atreides hawk crest above the breast pocket.
Hurry and dress, she said. Reverend Mother is waiting.
I dreamed of her once, Paul said. Who is she?
She was my teacher at the Bene Gesserit school. Now, she's the Emperor's Truthsayer. And Paul . . .  She hesitated. You must tell her about your dreams.
I will. Is she the reason we got Arrakis?
We did not get Arrakis. Jessica flicked dust from a pair of trousers, hung them with the jacket on the dressing stand beside his bed. Don't keep Reverend Mother waiting.
Paul sat up, hugged his knees. What's a gom jabbar?
Again, the training she had given him exposed her almost invisible hesitation, a nervous betrayal he felt as fear.
Jessica crossed to the window, flung wide the draperies, stared across the river orchards toward Mount Syubi . You'll learn about . . . the gom jabbar soon enough, she said.
He heard the fear in her voice and wondered at it.
Jessica spoke without turning. Reverend Mother is waiting in my morning room. Please hurry.
The Reverend Mother Gaius Helen Mohiam sat in a tapestried chair watching mother and son approach. Windows on each side of her overlooked the curving southern bend of the river and the green farmlands of the Atreides family holding, but the Reverend Mother ignored the view. She was feeling her age this morning, more than a little petulant. She blamed it on space travel and association with that abominable Spacing Guild and its secretive ways. But here was a mission that required personal attention from a Bene Gesserit-with-the-Sight. Even the Padishah Emperor's Truthsayer couldn't evade that responsibility when the duty call came.
Damn that Jessica! the Reverend Mother thought. If only she'd borne us a girl as she was ordered to do!
Jessica stopped three paces from the chair, dropped a small curtsy, a gentle flick of left hand along the line of her skirt. Paul gave the short bow his dancing master had taught - the one used when in doubt of another's station.
The nuances of Paul's greeting were not lost on the Reverend Mother. She said: He's a cautious one, Jessica.
Jessica's hand went to Paul's shoulder, tightened there. For a heartbeat, fear pulsed through her palm. Then she had herself under control. Thus he has been taught, Your Reverence.
What does she fear? Paul wondered.
The old woman studied Paul in one gestalten flicker: face oval like Jessica's, but strong bones . . . hair: the Duke's black-black but with browline of the maternal grandfather who cannot be named, and that thin, disdainful nose; shape of directly staring green eyes: like the old Duke, the paternal grandfather who is dead.
Now, there was a man who appreciated the power of bravura - even in death , the Reverend Mother thought.
Teaching is one thing, she said, the basic ingredient is another. We shall see. The old eyes darted a hard glance at Jessica. Leave us. I enjoin you to practice the meditation of peace.
Jessica took her hand from Paul's shoulder. Your Reverence, I - 
Jessica, you know it must be done.
Paul looked up at his mother, puzzled.
Jessica straightened. Yes . . . of course.
Paul looked back at the Reverend Mother. Politeness and his mother's obvious awe of this old woman argued caution. Yet he felt an angry apprehension at the fear he sensed radiating from his mother.
Paul . . .  Jessica took a deep breath. . . . this test you're about to receive . . . it's important to me.
Test? He looked up at her.
Remember that you're a duke's son, Jessica said. She whirled and strode from the room in a dry swishing of skirt. The door closed solidly behind her.
Paul faced the old woman, holding anger in check. Does one dismiss the Lady Jessica as though she were a serving wench?
A smile flicked the corners of the wrinkled old mouth. The Lady Jessica was my serving wench, lad, for fourteen years at school. She nodded. And a good one, too. Now, you come here!
The command whipped out at him. Paul found himself obeying before he could think about it. Using the Voice on me , he thought. He stopped at her gesture, standing beside her knees.
See this? she asked. From the folds of her gown, she lifted a green metal cube about fifteen centimeters on a side. She turned it and Paul saw that one side was open - black and oddly frightening. No light penetrated that open blackness.
Put your right hand in the box, she said.
Fear shot through Paul. He started to back away, but the old woman said: Is this how you obey your mother?
He looked up into bird-bright eyes.
Slowly, feeling the compulsions and unable to inhibit them, Paul put his hand into the box. He felt first a sense of cold as the blackness closed around his hand, then slick metal against his fingers and a prickling as though his hand were asleep.
A predatory look filled the old woman's features. She lifted her right hand away from the box and poised the hand close to the side of Paul's neck. He saw a glint of metal there and started to turn toward. . .
Stop! she snapped.
Using the Voice again! He swung his attention back to her face.
I hold at your neck the gom jabbar, she said. The gom jabbar, the high-handed enemy. It's a needle with a drop of poison on its tip. Ah-ah! Don't pull away or you'll feel that poison.
Paul tried to swallow in a dry throat. He could not take his attention from the seamed old face, the glistening eyes, the pale gums around silvery metal teeth that flashed as she spoke.
A duke's son must know about poisons, she said. It's the way of our times, eh? Musky, to be poisoned in your drink. Aumas, to be poisoned in your food. The quick ones and the slow ones and the ones in between. Here's a new one for you: the gom jabbar. It kills only animals.
Pride overcame Paul's fear. You dare suggest a duke's son is an animal? he demanded.
Let us say I suggest you may be human, she said. Steady! I warn you not to try jerking away. I am old, but my hand can drive this needle into your neck before you escape me.
Who are you? he whispered. How did you trick my mother into leaving me alone with you? Are you from the Harkonnens?
The Harkonnens? Bless us, no! Now, be silent. A dry finger touched his neck and he stilled the involuntary urge to leap away.
Good, she said. You pass the first test. Now, here's the way of the rest of it: If you withdraw your hand from the box you die. This is the only rule. Keep your hand in the box and live. Withdraw it and die.
Paul took a deep breath to still his trembling. If I call out there'll be servants on you in seconds and you'll die.
Servants will not pass your mother who stands guard outside that door. Depend on it. Your mother survived this test. Now it's your turn. Be honored. We seldom administer this to men-children.
Curiosity reduced Paul's fear to a manageable level. He heard truth in the old woman's voice, no denying it. If his mother stood guard out there . . . if this were truly a test . . . And whatever it was, he knew himself caught in it, trapped by that hand at his neck: the gom jabbar. He recalled the response from the Litany against Fear as his mother had taught him out of the Bene Gesserit rite.
I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain .
He felt calmness return, said: Get on with it, old woman.
Old woman! she snapped. You've courage, and that can't be denied. Well, we shall see, sirra. She bent close, lowered her voice almost to a whisper. You will feel pain in this hand within the box. Pain. But! Withdraw the hand and I'll touch your neck with my gom jabbar - the death so swift it's like the fall of the headsman's axe. Withdraw your hand and the gom jabbar takes you. Understand?
What's in the box?
Pain.
He felt increased tingling in his hand, pressed his lips tightly together. How could this be a test? he wondered. The tingling became an itch.
The old woman said; You've heard of animals chewing off a leg to escape a trap? There's an animal kind of trick. A human would remain in the trap, endure the pain, feigning death that he might kill the trapper and remove a threat to his kind.
The itch became the faintest burning. Why are you doing this? he demanded.
To determine if you're human. Be silent.
Paul clenched his left hand into a fist as the burning sensation increased in the other hand. It mounted slowly: heat upon heat upon heat . . . upon heat. He felt the fingernails of his free hand biting the palm. He tried to flex the fingers of the burning hand, but couldn't move them.
It burns, he whispered.
Silence!
Pain throbbed up his arm. Sweat stood out on his forehead. Every fiber cried out to withdraw the hand from that burning pit . . . but . . . the gom jabbar. Without turning his head, he tried to move his eyes to see that terrible needle poised beside his neck. He sensed that he was breathing in gasps, tried to slow his breaths and couldn't.
Pain!
His world emptied of everything except that hand immersed in agony, the ancient face inches away staring at him.
His lips were so dry he had difficulty separating them.
The burning! The burning!
He thought he could feel skin curling black on that agonized hand, the flesh crisping and dropping away until only charred bones remained.
It stopped!
As though a switch had been turned off, the pain stopped.
Paul felt his right arm trembling, felt sweat bathing his body.
Enough, the old woman muttered. Kull wahad! No woman child ever withstood that much. I must've wanted you to fail. She leaned back, withdrawing the gom jabbar from the side of his neck. Take your hand from the box, young human, and look at it.
He fought down an aching shiver, stared at the lightless void where his hand seemed to remain of its own volition. Memory of pain inhibited every movement. Reason told him he would withdraw a blackened stump from that box.
Do it! she snapped.
He jerked his hand from the box, stared at it astonished. Not a mark. No sign of agony on the flesh. He held up the hand, turned it, flexed the fingers.
Pain by nerve induction, she said. Can't go around maiming potential humans. There're those who'd give a pretty for the secret of this box, though. She slipped it into the folds of her gown.
But the pain -  he said.
Pain, she sniffed. A human can override any nerve in the body.
Paul felt his left hand aching, uncurled the clenched fingers, looked at four bloody marks where fingernails had bitten his palm. He dropped the hand to his side, looked at the old woman. You did that to my mother once?
Ever sift sand through a screen? she asked.
The tangential slash of her question shocked his mind into a higher awareness: Sand through a screen , he nodded.
We Bene Gesserit sift people to find the humans.
He lifted his right hand, willing the memory of the pain. And that's all there is to it - pain?
I observed you in pain, lad. Pain's merely the axis of the test. Your mother's told you about our ways of observing. I see the signs of her teaching in you. Our test is crisis and observation.
He heard the confirmation in her voice, said: It's truth!
She stared at him. He senses truth! Could he be the one? Could he truly be the one? She extinguished the excitement, reminding herself: Hope clouds observation .
You know when people believe what they say, she said.
I know it.
The harmonics of ability confirmed by repeated test were in his voice. She heard them, said: Perhaps you are the Kwisatz Haderach. Sit down, little brother, here at my feet.
I prefer to stand.
Your mother sat at my feet once.
I'm not my mother.
You hate us a little, eh? She looked toward the door, called out: Jessica!
The door flew open and Jessica stood there staring hard-eyed into the room. Hardness melted from her as she saw Paul. She managed a faint smile.
Jessica, have you ever stopped hating me? the old woman asked.
I both love and hate you, Jessica said. The hate - that's from pains I must never forget. The love - that's . . . 
Just the basic fact, the old woman said, but her voice was gentle. You may come in now, but remain silent. Close that door and mind it that no one interrupts us.
Jessica stepped into the room, closed the door and stood with her back to it. My son lives , she thought. My son lives and is . . . human. I knew he was . . . but . . . he lives. Now, I can go on living . The door felt hard and real against her back. Everything in the room was immediate and pressing against her senses.
My son lives .
Paul looked at his mother. She told the truth . He wanted to get away alone and think this experience through, but knew he could not leave until he was dismissed. The old woman had gained a power over him. They spoke truth . His mother had undergone this test. There must be terrible purpose in it . . . the pain and fear had been terrible. He understood terrible purposes. They drove against all odds. They were their own necessity. Paul felt that he had been infected with terrible purpose. He did not know yet what the terrible purpose was.
Some day, lad, the old woman said, you, too, may have to stand outside a door like that. It takes a measure of doing.
Paul looked down at the hand that had known pain, then up to the Reverend Mother. The sound of her voice had contained a difference then from any other voice in his experience. The words were outlined in brilliance. There was an edge to them. He felt that any question he might ask her would bring an answer that could lift him out of his flesh-world into something greater.
Why do you test for humans? he asked.
To set you free.
Free?
Once men turned their thinking over to machines in the hope that this would set them free. But that only permitted other men with machines to enslave them.
'Thou shalt not make a machine in the likeness of a man's mind,'  Paul quoted.
Right out of the Butlerian Jihad and the Orange Catholic Bible, she said. But what the O.C. Bible should've said is: 'Thou shalt not make a machine to counterfeit a human mind.' Have you studied the Mentat in your service?
I've studied with Thufir Hawat.
The Great Revolt took away a crutch, she said. It forced human minds to develop. Schools were started to train human talents.
Bene Gesserit schools?
She nodded. We have two chief survivors of those ancient schools: the Bene Gesserit and the Spacing Guild. The Guild, so we think, emphasizes almost pure mathematics. Bene Gesserit performs another function.
Politics, he said.
Kull wahad! the old woman said. She sent a hard glance at Jessica.
I've not told him. Your Reverence, Jessica said.
The Reverend Mother returned her attention to Paul. You did that on remarkably few clues, she said. Politics indeed. The original Bene Gesserit school was directed by those who saw the need of a thread of continuity in human affairs. They saw there could be no such continuity without separating human stock from animal stock - for breeding purposes.
The old woman's words abruptly lost their special sharpness for Paul. He felt an offense against what his mother called his instinct for rightness . It wasn't that Reverend Mother lied to him. She obviously believed what she said. It was something deeper, something tied to his terrible purpose.
He said: But my mother tells me many Bene Gesserit of the schools don't know their ancestry.
The genetic lines are always in our records, she said. Your mother knows that either she's of Bene Gesserit descent or her stock was acceptable in itself.
Then why couldn't she know who her parents are?
Some do . . . Many don't. We might, for example, have wanted to breed her to a close relative to set up a dominant in some genetic trait. We have many reasons.
Again, Paul felt the offense against rightness. He said: You take a lot on yourselves.
The Reverend Mother stared at him, wondering: Did I hear criticism in his voice? We carry a heavy burden, she said.
Paul felt himself coming more and more out of the shock of the test. He leveled a measuring stare at her, said: You say maybe I'm the . . . Kwisatz Haderach. What's that, a human gom jabbar?
Paul, Jessica said. You mustn't take that tone with - 
I'll handle this, Jessica, the old woman said. Now, lad, do you know about the Truthsayer drug?
You take it to improve your ability to detect falsehood, he said. My mother's told me.
Have you ever seen truthtrance?
He shook his head. No.
The drug's dangerous, she said, but it gives insight. When a Truthsayer's gifted by the drug, she can look many places in her memory - in her body's memory. We look down so many avenues of the past . . . but only feminine avenues. Her voice took on a note of sadness. Yet, there's a place where no Truthsayer can see. We are repelled by it, terrorized. It is said a man will come one day and find in the gift of the drug his inward eye. He will look where we cannot - into both feminine and masculine pasts.
Your Kwisatz Haderach?
Yes, the one who can be many places at once: the Kwisatz Haderach. Many men have tried the drug . . . so many, but none has succeeded.
They tried and failed, all of them?
Oh, no. She shook her head. They tried and died.
To attempt an understanding of Muad'Dib without understanding his mortal enemies, the Harkonnens, is to attempt seeing Truth without knowing Falsehood. It is the attempt to see the Light without knowing Darkness. It cannot be.
- from Manual of Muad'Dib by the Princess Irulan
It was a relief globe of a world, partly in shadows, spinning under the impetus of a fat hand that glittered with rings. The globe sat on a freeform stand at one wall of a windowless room whose other walls presented a patchwork of multicolored scrolls, filmbooks, tapes and reels. Light glowed in the room from golden balls hanging in mobile suspensor fields.
An ellipsoid desk with a top of jade-pink petrified elacca wood stood at the center of the room. Veriform suspensor chairs ringed it, two of them occupied. In one sat a dark-haired youth of about sixteen years, round of face and with sullen eyes. The other held a slender, short man with effeminate face.
Both youth and man stared at the globe and the man half-hidden in shadows spinning it.
A chuckle sounded beside the globe. A basso voice rumbled out of the chuckle: There it is, Piter - the biggest mantrap in all history. And the Duke's headed into its jaws. Is it not a magnificent thing that I, the Baron Vladimir Harkonnen, do?
Assuredly, Baron, said the man. His voice came out tenor with a sweet, musical quality.
The fat hand descended onto the globe, stopped the spinning. Now, all eyes in the room could focus on the motionless surface and see that it was the kind of globe made for wealthy collectors or planetary governors of the Empire. It had the stamp of Imperial handicraft about it. Latitude and longitude lines were laid in with hair-fine platinum wire. The polar caps were insets of finest cloud-milk diamonds.
The fat hand moved, tracing details on the surface. I invite you to observe, the basso voice rumbled. Observe closely, Piter, and you, too, Feyd-Rautha, my darling: from sixty degrees north to seventy degrees south - these exquisite ripples. Their coloring: does it not remind you of sweet caramels? And nowhere do you see blue of lakes or rivers or seas. And these lovely polar caps - so small. Could anyone mistake this place? Arrakis! Truly unique. A superb setting for a unique Victory.
A smile touched Piter's lips. And to think. Baron: the Padishah Emperor believes he's given the Duke your spice planet. How poignant.
That's a nonsensical statement, the Baron rumbled. You say this to confuse young Feyd-Rautha, but it is not necessary to confuse my nephew.
The sullen-faced youth stirred in his chair, smoothed a wrinkle in the black leotards he wore. He sat upright as a discreet tapping sounded at the door in the wall behind him.
Piter unfolded from his chair, crossed to the door, cracked it wide enough to accept a message cylinder. He closed the door, unrolled the cylinder and scanned it. A chuckle sounded from him. Another.
Well? the Baron demanded.
The fool answered us, Baron!
Whenever did an Atreides refuse the opportunity for a gesture? the Baron asked. Well, what does he say?
He's most uncouth, Baron. Addresses you as 'Harkonnen' - no 'Sire et Cher Cousin,' no title, nothing.
It's a good name, the Baron growled, and his voice betrayed his impatience. What does dear Leto say?
He says: 'Your offer of a meeting is refused. I have ofttimes met your treachery and this all men know.' 
And? the Baron asked.
He says: 'The art of kanly still has admirers in the Empire. ' He signs it: 'Duke Leto of Arrakis.'  Piter began to laugh. Of Arrakis! Oh, my! This is almost too rich!
Be silent, Piter, the Baron said, and the laughter stopped as though shut off with a switch. Kanly, is it? the Baron asked. Vendetta, heh? And he uses the nice old word so rich in tradition to be sure I know he means it.
You made the peace gesture, Piter said. The forms have been obeyed.
For a Mentat, you talk too much, Piter, the Baron said. And he thought: I must do away with that one soon. He has almost outlived his usefulness . The Baron stared across the room at his Mental assassin, seeing the feature about him that most people noticed first: the eyes, the shaded slits of blue within blue, the eyes without any white in them at all.
A grin flashed across Piter's face. It was like a mask grimace beneath those eyes like holes. But, Baron! Never has revenge been more beautiful. It is to see a plan of the most exquisite treachery: to make Leto exchange Caladan for Dune - and without alternative because the Emperor orders it. How waggish of you!
In a cold voice, the Baron said: You have a flux of the mouth, Piter.
But I am happy, my Baron. Whereas you . . . you are touched by jealousy.
Piter!
Ah-ah. Baron! Is it not regrettable you were unable to devise this delicious scheme by yourself?
Someday I will have you strangled, Piter.
Of a certainty, Baron. Enfin! But a kind act is never lost, eh?
Have you been chewing verite or semuta, Piter?
Truth without fear surprises the Baron, Piter said. His face drew down into a caricature of a frowning mask. Ah, hah! But you see, Baron, I know as a Mentat when you will send the executioner. You will hold back just so long as I am useful. To move sooner would be wasteful and I'm yet of much use. I know what it is you learned from that lovely Dune planet - waste not. True, Baron?
The Baron continued to stare at Piter.
Feyd-Rautha squirmed in his chair. These wrangling fools! he thought. My uncle cannot talk to his Mental without arguing. Do they think I've nothing to do except listen their arguments?
Feyd, the Baron said. I told you to listen and learn when I invited you in here. Are you learning?
Yes, Uncle. the voice was carefully subservient.
Sometimes I wonder about Piter, the Baron said. I cause pain out of necessity, but he . . . I swear he takes a positive delight in it. For myself, I can feel pity toward the poor Duke Leto. Dr. Yueh will move against him soon, and that'll be the end of all the Atreides. But surely Leto will know whose hand directed the pliant doctor . . . and knowing that will be a terrible thing.
Then why haven't you directed the doctor to slip a kindjal between his ribs quietly and efficiently? Piter asked. You talk of pity, but - 
The Duke must know when I encompass his doom, the Baron said. And the other Great Houses must learn of it. The knowledge will give them pause. I'll gain a bit more room to maneuver. The necessity is obvious, but I don't have to like it.
Room to maneuver, Piter sneered. Already you have the Emperor's eyes on you, Baron. You move too boldly. One day the Emperor will send a legion or two of his Sardaukar down here onto Giedi Prime and that'll be an end to the Baron Vladimir Harkonnen.
You'd like to see that, wouldn't you, Piter? the Baron asked. You'd enjoy seeing the Corps of Sardaukar pillage through my cities and sack this castle. You'd truly enjoy that.
Does the Baron need to ask? Piter whispered.
You should've been a Bashar of the Corps, the Baron said. You're too interested in blood and pain. Perhaps I was too quick with my promise of the spoils of Arrakis.
Piter took five curiously mincing steps into the room, stopped directly behind Feyd-Rautha. There was a tight air of tension in the room, and the youth looked up at Piter with a worried frown.
Do not toy with Piter, Baron, Piter said. You promised me the Lady Jessica. You promised her to me.
For what, Piter? the Baron asked. For pain?
Piter stared at him, dragging out the silence.
Feyd-Rautha moved his suspensor chair to one side, said: Uncle, do I have to stay? You said you'd - 
My darling Feyd-Rautha grows impatient, the Baron said. He moved within the shadows beside the globe. Patience, Feyd. And he turned his attention back to the Mentat. What of the Dukeling, the child Paul, my dear Piter?
The trap will bring him to you, Baron, Piter muttered.
That's not my question, the Baron said. You'll recall that you predicted the Bene Gesserit witch would bear a daughter to the Duke. You were wrong, eh, Mentat?
I'm not often wrong, Baron, Piter said, and for the first time there was fear in his voice. Give me that: I'm not often wrong. And you know yourself these Bene Gesserit bear mostly daughters. Even the Emperor's consort had produced only females.
Uncle, said Feyd-Rautha, you said there'd be something important here for me to - 
Listen to my nephew, the Baron said. He aspires to rule my Barony, yet he cannot rule himself. The Baron stirred beside the globe, a shadow among shadows. Well then, Feyd-Rautha Harkonnen, I summoned you here hoping to teach you a bit of wisdom. Have you observed our good Mentat? You should've learned something from this exchange.
But, Uncle - 
A most efficient Mentat, Piter, wouldn't you say, Feyd?
Yes, but - 
Ah! Indeed but! But he consumes too much spice, eats it like candy. Look at his eyes! He might've come directly from the Arrakeen labor pool. Efficient, Piter, but he's still emotional and prone to passionate outbursts. Efficient, Piter, but he still can err.
Piter spoke in a low, sullen tone: Did you call me in here to impair my efficiency with criticism, Baron?
Impair your efficiency? You know me better, Piter. I wish only for my nephew to understand the limitations of a Mentat.
Are you already training my replacement? Piter demanded.
Replace you? Why, Piter, where could I find another Mentat with your cunning and venom?
The same place you found me, Baron.
Perhaps I should at that, the Baron mused. You do seem a bit unstable lately. And the spice you eat!
Are my pleasures too expensive, Baron? Do you object to them?
My dear Piter, your pleasures are what tie you to me. How could I object to that? I merely wish my nephew to observe this about you.
Then I'm on display, Piter said. Shall I dance? Shall I perform my various functions for the eminent Feyd-Rau - 
Precisely, the Baron said. You are on display. Now, be silent. He glanced at Feyd-Rautha, noting his nephew's lips, the full and pouting look of them, the Harkonnen genetic marker, now twisted slightly in amusement. This is a Mentat, Feyd. It has been trained and conditioned to perform certain duties. The fact that it's encased in a human body, however, must not be overlooked. A serious drawback, that. I sometimes think the ancients with their thinking machines had the right idea.
They were toys compared to me, Piter snarled. You yourself, Baron, could outperform those machines .
Perhaps, the Baron said. Ah, well . . .  He took a deep breath, belched. Now, Piter, outline for my nephew the salient features of our campaign against the House of Atreides. Function as a Mentat for us, if you please.
Baron, I've warned you not to trust one so young with this information. My observations of - 
I'll be the judge of this, the Baron said. I give you an order, Mentat. Perform one of your various functions.
So be it, Piter said. He straightened, assuming an odd attitude of dignity - as though it were another mask, but this time clothing his entire body. In a few days Standard, the entire household of the Duke Leto will embark on a Spacing Guild liner for Arrakis. The Guild will deposit them at the city of Arrakeen rather than at our city of Carthag . The Duke's Mentat, Thufir Hawat, will have concluded rightly that Arrakeen is easier to defend.
'''

    functions = '''\
// Random words from words.txt
const char *words[] = {
	{{WORDS}}
};\
'''

    # Create words string
    word_arr_str = create_words_string(words, words_num)

    # Read the content of the input file
    with open("./src/main.c", 'r') as file:
        content = file.read()

    # Replace the template
    modified_content = content.replace("{{FUNCTIONS}}", functions + "\n{{FUNCTIONS}}")\
                              .replace("{{WORDS}}", word_arr_str)

    # Write the modified content to the output file
    with open("./src/main.c", 'w') as file:
        file.write(modified_content)

    return