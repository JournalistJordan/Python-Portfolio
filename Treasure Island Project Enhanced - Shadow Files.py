# Spy Detective Game by Jordan Foltz 3/10/2026
print(r'''
 *********************************************************************************
  .OOOOOOOOOOOOOOO @@         D i c k  T r a c y        @@ OOOOOOOOOOOOOOOO.
  OOOOOOOOOOOOOOOO @@                                    @@ OOOOOOOOOOOOOOOO
  OOOOOOOOOO'''''' @@                                    @@ ```````OOOOOOOOO
  OOOOO'' aaa@@@@@@@@@@@@@@@@@@@@"""                   """""""""@@aaaa `OOOO
  OOOOO,""""@@@@@@@@@@@@@@""""                                     a@"" OOOA
  OOOOOOOOOoooooo,                                            |OOoooooOOOOOS
  OOOOOOOOOOOOOOOOo,            I'll be selling the           |OOOOOOOOOOOOC
  OOOOOOOOOOOOOOOOOO            house and moving my          ,|OOOOOOOOOOOOI
  OOOOOOOOOOOOOOOOOO @           family to a condo           |OOOOOOOOOOOOOI
  OOOOOOOOOOOOOOOOO'@           complex with a pool          OOOOOOOOOOOOOOb
  OOOOOOOOOOOOOOO'a'            & where someone else         |OOOOOOOOOOOOOy
  OOOOOOOOOOOOOO''              mows the grass!           aa`OOOOOOOOOOOP
  OOOOOOOOOOOOOOb,..            Things here will be           `@aa``OOOOOOOh
  OOOOOOOOOOOOOOOOOOo           hectic for the next             `@@@aa OOOOo
  OOOOOOOOOOOOOOOOOOO|          6 weeks or so.                     @@@ OOOOe
  OOOOOOOOOOOOOOOOOOO@                               aaaaaaa       @@',OOOOn
  OOOOOOOOOOOOOOOOOOO@                        aaa@@@@@@@@""        @@ OOOOOi
  OOOOOOOOOO~~ aaaaaa"a                 aaa@@@@@@@@@@""            @@ OOOOOx
  OOOOOO aaaa@"""""""" ""            @@@@@@@@@@@@""               @@@|`OOOO'
  OOOOOOOo`@@a                  aa@@  @@@@@@@""         a@        @@@@ OOOO9
  OOOOOOO'  `@@a               @@a@@   @@""           a@@   a     |@@@ OOOO3
  `OOOO'       `@    aa@@       aaa"""          @a        a@     a@@@',OOOO'
 *                                                                               *
 *                       🔍 OPERATION: SHADOW FILES 🔍                   *
 *                                                                               *
 *********************************************************************************
''')
 
print("Welcome to Operation: Shadow Files.")
print("Your mission: Infiltrate the enemy headquarters and recover the classified documents.")
print("You have access to your standard spy kit: grappling hook, smoke bombs, and hacking device.")
input("Press enter to continue...")
 
# Arrival and Decision
print("You arrive outside the enemy headquarters. It's heavily guarded with multiple security layers.")
print("You observe the facility for 10 minutes and notice three potential approaches.")
approach_decision = (input('Type "stealth", "disguise", or "brute force" ')).lower()
 
if approach_decision == "stealth":
    print("You choose the stealth route. Your training kicks in as you scan for vulnerabilities.")
    print("You spot four entry points: ventilation shaft, sewer access, roof access, or underground tunnel.")
    entry_decision = (input('Do you take the "ventilation", "sewer", "roof", or "tunnel"? ')).lower()
    
    if entry_decision == "ventilation":
        print("You expertly climb to the roof and locate the ventilation intake.")
        print("The shaft is narrow and dark. You have your grappling hook and night vision goggles.")
        vent_choice = (input('Use "grappling hook" to descend or "night vision" to navigate carefully? ')).lower()
        
        if vent_choice == "night vision":
            print("With night vision active, you spot motion sensors and laser tripwires.")
            print("You carefully navigate around them and reach a junction with three paths.")
            junction_decision = (input('Take "left" to server room, "right" to executive offices, or "straight" to security room? ')).lower()
            
            if junction_decision == "straight":
                print("You reach the security room and find three computer terminals.")
                print("Each terminal has different security levels visible on their screens.")
                terminal_decision = (input('Which terminal do you access? "red" (high security), "blue" (medium), or "green" (low)? ')).lower()
                
                if terminal_decision == "green":
                    print("Excellent choice! The green terminal has minimal security.")
                    print("You access the building schematics and discover a secret passage to the vault.")
                    print("Do you follow the secret passage or try to access the vault directly?")
                    vault_approach = (input('Type "secret passage" or "direct access": ')).lower()
                    
                    if vault_approach == "secret passage":
                        print("The passage leads to a hidden elevator behind a bookshelf.")
                        print("You arrive at the vault level. A guard is stationed at the vault door.")
                        guard_handling = (input('Do you "sedate", "distract", or "hack" the guard\'s communications? ')).lower()
                        
                        if guard_handling == "hack":
                            print("You hack into the guard's radio and create a false emergency report.")
                            print("The guard rushes away, leaving the vault unattended. Victory!")
                            print("You recover the Shadow Files and escape through the secret passage. MISSION ACCOMPLISHED! YOU WIN!")
                        elif guard_handling == "sedate":
                            print("You use your tranquilizer dart, but another guard rounds the corner immediately.")
                            print("You're caught in the act. Mission failed... YOU LOSE.")
                        else:
                            print("Your distraction attempt fails and the guard calls for backup.")
                            print("You're surrounded before you can react. Mission failed... YOU LOSE.")
                    else:
                        print("You try to access the vault directly but trigger pressure plate alarms.")
                        print("The entire facility goes into lockdown. Mission failed... YOU LOSE.")
                        
                elif terminal_decision == "red":
                    print("The red terminal was connected to the main security system!")
                    print("Alarms blare as you're locked inside the security room.")
                    print("Guards storm the room. You're captured and interrogated. Mission failed... YOU LOSE.")
                elif terminal_decision == "blue":
                    print("The blue terminal was a honeypot trap!")
                    print("It releases knockout gas and locks all ventilation shafts.")
                    print("You lose consciousness and wake up in handcuffs. Mission failed... YOU LOSE.")
                else:
                    print("You hesitate too long and a security patrol spots you on camera.")
                    print("They're on their way. You have no escape route. Mission failed... YOU LOSE.")
                    
            elif junction_decision == "left":
                print("You reach the server room, but it's protected by a biometric scanner.")
                print("You notice a maintenance worker nearby. What's your move?")
                server_approach = (input('Do you "impersonate" the worker, "hack" the scanner, or "create diversion"? ')).lower()
                
                if server_approach == "impersonate":
                    print("You knock out the worker and take their uniform.")
                    print("The scanner accepts the worker's credentials. You're in!")
                    print("The servers contain encrypted files. You need to decrypt them.")
                    decrypt_choice = (input('Use "brute force", "social engineering", or "backdoor access"? ')).lower()
                    
                    if decrypt_choice == "backdoor access":
                        print("Your hacking device finds a vulnerability in the system.")
                        print("You extract the Shadow Files and create a data trail pointing to a rival agency.")
                        print("Perfect misdirection! You escape cleanly. MISSION ACCOMPLISHED! YOU WIN!")
                    else:
                        print("Your decryption attempt triggers security protocols.")
                        print("The system locks down and alerts security. Mission failed... YOU LOSE.")
                else:
                    print("Your approach fails and security is alerted to your presence.")
                    print("You're forced to retreat empty-handed. Mission failed... YOU LOSE.")
                    
            else:
                print("You reach the executive offices but encounter the head of security.")
                print("He recognizes you from an old mission briefing. You're exposed!")
                print("A fierce fight breaks out, but you're outnumbered. Mission failed... YOU LOSE.")
                
        else:
            print("The grappling hook makes too much noise and alerts rooftop snipers.")
            print("You're pinned down and captured. Mission failed... YOU LOSE.")
            
    elif entry_decision == "sewer":
        print("You enter through the sewer system. It's disgusting but effective.")
        print("After navigating through maze-like tunnels, you reach a fork.")
        sewer_choice = (input('Go "up" to the basement or "forward" to the sub-basement? ')).lower()
        
        if sewer_choice == "up":
            print("You emerge in the basement laundry room.")
            print("Two maintenance workers are chatting nearby. What do you do?")
            laundry_decision = (input('Do you "hide", "blend in", or "create distraction"? ')).lower()
            
            if laundry_decision == "blend in":
                print("You grab a uniform and push a laundry cart. Perfect cover!")
                print("You're approached by a suspicious-looking employee asking questions.")
                interrogation_response = (input('Do you "play dumb", "use fake credentials", or "bribe"? ')).lower()
                
                if interrogation_response == "use fake credentials":
                    print("Your fake ID passes inspection. You're granted access to the elevators.")
                    print("You head to the 13th floor where the vault is located.")
                    print("But the elevator stops at floor 7 and armed agents board. Quick thinking!")
                    elevator_choice = (input('Do you "press emergency stop", "use smoke bomb", or "play it cool"? ')).lower()
                    
                    if elevator_choice == "smoke bomb":
                        print("The smoke bomb creates chaos! You escape during the confusion.")
                        print("You reach the vault and use your hacking device to crack the lock.")
                        print("The Shadow Files are yours! You escape through the service stairs. MISSION ACCOMPLISHED! YOU WIN!")
                    else:
                        print("Your choice fails and the agents recognize you from wanted posters.")
                        print("You're arrested after a brief struggle. Mission failed... YOU LOSE.")
                else:
                    print("Your response raises suspicion and security is called.")
                    print("You're captured before you can reach the vault. Mission failed... YOU LOSE.")
            else:
                print("Your choice leads to discovery. The workers sound the alarm.")
                print("You're caught in the basement. Mission failed... YOU LOSE.")
        else:
            print("The sub-basement is flooded and you're trapped.")
            print("The water level rises and you're forced to call for rescue.")
            print("Your cover is blown. Mission failed... YOU LOSE.")
            
    elif entry_decision == "roof":
        print("You scale the building using your grappling hook and climbing gear.")
        print("On the roof, you encounter a helicopter landing pad with a guard patrol.")
        roof_decision = (input('Do you "ambush" the patrol, "sneak past", or "sabotage" their communications? ')).lower()
        
        if roof_decision == "sabotage":
            print("You disable their communications, creating confusion.")
            print("You find a roof access door and descend to the penthouse level.")
            print("The penthouse belongs to the CEO, who's hosting a party tonight.")
            party_decision = (input('Do you "crash the party", "sneak through", or "wait it out"? ')).lower()
            
            if party_decision == "crash the party":
                print("You blend in with the guests using your charm and fake credentials.")
                print("The CEO approaches you, thinking you're an important guest.")
                ceo_interaction = (input('Do you "flirt", "discuss business", or "slip something" in their drink? ')).lower()
                
                if ceo_interaction == "flirt":
                    print("Your charm works! The CEO invites you to their private office.")
                    print("In the office, you spot the vault behind a painting.")
                    print("While the CEO is distracted, you access the vault and recover the files.")
                    print("You make your escape during the party chaos. MISSION ACCOMPLISHED! YOU WIN!")
                else:
                    print("Your approach fails and the CEO's security detail becomes suspicious.")
                    print("You're escorted out and arrested. Mission failed... YOU LOSE.")
            else:
                print("Your choice leads to discovery. Security finds you hiding.")
                print("You're captured before reaching your objective. Mission failed... YOU LOSE.")
        else:
            print("Your approach fails and rooftop security alerts the entire facility.")
            print("You're surrounded with no escape route. Mission failed... YOU LOSE.")
            
    else:
        print("The tunnel leads to a dead end - it was a trap set by counter-intelligence.")
        print("The walls close in and you're captured. Mission failed... YOU LOSE.")
 
elif approach_decision == "disguise":
    print("You choose disguise. Your agency provided three cover identities.")
    print("Which identity will you assume?")
    identity_choice = (input('Type "IT technician", "janitor", or "executive consultant": ')).lower()
    
    if identity_choice == "it technician":
        print("Perfect choice! You arrive with a fake work order for 'network maintenance'.")
        print("The guard at reception calls IT to verify your identity.")
        verification_response = (input('Do you "use voice modulator", "social engineer", or "hack their system"? ')).lower()
        
        if verification_response == "social engineer":
            print("You convince the guard that the IT systems are down and verification is impossible.")
            print("He lets you through. You head to the server room on floor 8.")
            print("The server room requires two-factor authentication. You have options:")
            auth_method = (input('Use "RFID cloner", "shoulder surf", or "create emergency"? ')).lower()
            
            if auth_method == "create emergency":
                print("You trigger a fake fire alarm, causing chaos and evacuation.")
                print("During the confusion, you slip into the server room.")
                print("The Shadow Files are on the main server, but they're heavily encrypted.")
                encryption_solution = (input('Do you "use quantum decryptor", "find backdoor", or "extract physically"? ')).lower()
                
                if encryption_solution == "find backdoor":
                    print("You discover a hidden maintenance account with default credentials.")
                    print("You access the files and plant false evidence pointing to a foreign power.")
                    print("Perfect misdirection! You escape during the evacuation. MISSION ACCOMPLISHED! YOU WIN!")
                else:
                    print("Your method triggers security alerts. You're caught in the act. Mission failed... YOU LOSE.")
            else:
                print("Your authentication attempt fails and biometric alarms trigger.")
                print("Security teams converge on your location. Mission failed... YOU LOSE.")
        else:
            print("Your verification fails and the guard becomes suspicious.")
            print("He calls security and you're arrested. Mission failed... YOU LOSE.")
            
    elif identity_choice == "janitor":
        print("You arrive early morning with cleaning supplies and a valid-looking badge.")
        print("You start cleaning but attract attention from the head of housekeeping.")
        housekeeping_challenge = (input('Do you "bribe", "flirt", or "demonstrate cleaning skills"? ')).lower()
        
        if housekeeping_challenge == "demonstrate cleaning skills":
            print("Your cleaning expertise impresses her! She gives you access to restricted areas.")
            print("You're assigned to clean the executive floor where the vault is located.")
            print("While cleaning, you discover the vault has a maintenance panel.")
            vault_access = (input('Do you "pick the lock", "use acid", or "find keycard"? ')).lower()
            
            if vault_access == "find keycard":
                print("You locate the master keycard in the supervisor's office.")
                print("You access the vault and find the Shadow Files in a secure container.")
                print("You replace the files with duplicates and escape with the originals. MISSION ACCOMPLISHED! YOU WIN!")
            else:
                print("Your method triggers silent alarms. Security captures you. Mission failed... YOU LOSE.")
        else:
            print("Your approach fails and she reports you to security.")
            print("You're arrested for suspicious behavior. Mission failed... YOU LOSE.")
            
    else:
        print("You arrive in an expensive suit with fake business credentials.")
        print("The receptionist asks for your appointment details.")
        executive_response = (input('Do you "name-drop", "show fake invitation", or "demand to see CEO"? ')).lower()
        
        if executive_response == "name-drop":
            print("You drop the name of a board member you researched beforehand.")
            print("It works! You're escorted to the executive lounge.")
            print("While waiting, you overhear the vault code being discussed.")
            code_approach = (input('Do you "memorize code", "record conversation", or "follow speaker"? ')).lower()
            
            if code_approach == "memorize code":
                print("You commit the code to memory and wait for the right moment.")
                print("During lunch break, you access the vault using the code.")
                print("The Shadow Files are yours! You walk out like you belong there. MISSION ACCOMPLISHED! YOU WIN!")
            else:
                print("Your method is discovered and security is alerted.")
                print("You're captured before reaching the vault. Mission failed... YOU LOSE.")
        else:
            print("Your approach fails and security becomes suspicious.")
            print("You're escorted out and arrested. Mission failed... YOU LOSE.")
 
elif approach_decision == "brute force":
    print("You decide on a direct assault. This is risky but might work with the right strategy.")
    print("You have three options for your attack plan.")
    brute_method = (input('Do you use "explosives", "hostage situation", or "full assault"? ')).lower()
    
    if brute_method == "explosives":
        print("You plant charges at strategic points but trigger silent alarms.")
        print("The building evacuates but elite counter-terrorism team arrives.")
        counter_decision = (input('Do you "surrender", "fight back", or "use hostages"? ')).lower()
        
        if counter_decision == "fight back":
            print("You use your advanced combat training and gadgets effectively.")
            print("During the chaos, you reach the vault and grab the Shadow Files.")
            print("You escape through the chaos you created. MISSION ACCOMPLISHED! YOU WIN!")
        else:
            print("Your choice leads to your capture. Mission failed... YOU LOSE.")
    else:
        print("Your brute force method is countered by superior security measures.")
        print("You're overwhelmed and captured. Mission failed... YOU LOSE.")
 
else:
    print("You stand there paralyzed by indecision until a patrol car spots you.")
    print("You're arrested before you can even begin your mission. Mission failed... YOU LOSE.")
 
print("\nThanks for playing Operation: Shadow Files!")
print("Remember: In the world of espionage, every decision counts.")
print("The fate of nations rests in capable hands like yours.")
