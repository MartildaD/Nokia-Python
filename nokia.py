def main():
    print("""
Welcome to Nokia Menu 

 
1 Phone book
2 Messages
3 Chat
4 Call register
5 Tones
6 Settings
7 Call divert
8 Music
9 Games
10 Calculator
11 Reminders
12 Clock
13 Profiles
14 Services
15 Sim sevices
""")
    choice = int(input())

    match choice:
        case 1: 
            Phone_book()
        case 2: 
            Messages()
        case 3: 
            print("Opening Chat")
        case 4: 
            Call_register()
        case 5: 
            Tones()
        case 6: 
            Settings()
        case 7: 
            print("OPening Call divert")
        case 8: 
            Music()
        case 9: 
            print("Opening Games")
        case 10: 
            print("Opening Calculator")
        case 11: 
            print("OPening Reminders")
        case 12: 
            Clock()
        case 13: 
            print("Opening Profiles")
        case 14: 
            print("Opening Services")
        case 15: 
            print("Opening Sim_ sevices")
        case 0: 
            print("Invalid options")

def Phone_book():
    print("""
Phonebookmenu

1 Search
2 Service NOs
3 Add name
4 Erase
5 Edit
6 Copy
7 Assign tone
8 Send b'card
9 Options
10 Speed dials
11 Voice tags                          
""")
    choice = int(input())

    match choice:
        case 1: 
            print("Search")
        case 2: 
            print("Service NOs")
        case 3: 
            print("Add name")
        case 4: 
            print("Erase")
        case 5: 
            print("Edit")
        case 6: 
            print("Copy")
        case 7: 
            print("Assign tone")
        case 8: 
            print("Send b'card")
        case 9: 
            print("""
Options
1 Memory in use
2 Type of view
3 Memory status
""")

            Options_choice = int(input())
            match options_choice:
                    case 1: 
                        print("Memory in use")
                    case 2: 
                        print("Type of view")
                    case 3: 
                        print("Memory status")
                    case 0:
                         print("Invalid options")

        case 10: 
            print("Speed dials")
        case 11: 
            print("Voice tags")
        case 0: 
            print("Invalid options")

def Messages():
    print("""
Messagesmenu

1 Write messages
2 Inbox
3 Outbox
4 Picture messages
5 Templates
6 Smileys
7 Message settings
8 Info service
9 Voice mailbox number
10 Service command editor                     
""")
    choice = int(input())

    match choice:
        case 1: 
            print("Write messages")
        case 2: 
            print("Inbox")
        case 3: 
            print("Outbox")
        case 4: 
            print("Picture messages")
        case 5: 
            print("Templates")
        case 6: 
            print("Smileys")
        case 7: 
            print("""
Messagesettings
1 Set
2 Common
""")
            settings_choice = int(input())
            match settings_choice:
                case 1: 
                    print("""
Messagesset
1 Message centre number
2 Message sent as
3 Message validity
""")
                    set_choice = int(input())
                    match set_choice:
                        case 1: 
                            print("Message centre number")
                        case 2: 
                            print("Message sent as")
                        case 3: 
                            print("Message validity")
                        case 0: 
                            print("Invalid options")

                case 2: 
                    print("""
Messagescommon
1 Delivery report
2 Reply via same centre
3 Character support
""")
                    common_choice = int(input())

                    match common_choice:
                        case 1: 
                            print("Delivery report")
                        case 2: 
                            print("Reply via same centre")
                        case 3: 
                            print("Character support")
                        case 0: 
                            print("Invalid options")


        case 8: 
            print("Info service")
        case 9: 
            print("Voice mailbox number")
        case 10: 
            print("Service command editor")
        case 0: 
            print("Invalid options")

def Call_register():
    print("""
Callregistermenu

1 Missed calls
2 Received calls
3 Dialed numbers
4 Erase recent call lists
5 Show call duration
6 Show call costs
7 call cost settings
8 Prepaid credit                     
""")
    choice = int(input())

    match choice:
        case 1: 
            print("Missed calls")
        case 2: 
            print("Received calls")
        case 3: 
            print("Dialed numbers")
        case 4: 
            print("Erase recent call lists")
        case 5: 
            print("""
Showcallduration
1 Last call duration
2 All calls' duration
3 Received calls' duration 
4 Dialed calls' duration
5 clear timers
""")
            showcallduration_choice = int(input())
            match showcallduration_choice:
                case 1: 
                    print("Last call duration")
                case 2: 
                    print("All calls' duration")
                case 3: 
                    print("Received calls' duration")
                case 4: 
                    print("Dialed calls' duration")
                case 5: 
                    print("clear timers")
                case 0: 
                    print("Invalid options")

        case 6: 
            print("""
Showcallcosts
1 Last call cost
2 All calls' cost
3 Clear counters
""")
            showcallcosts_choice = int(input())
            match showcallcosts_choice:
                case 1: 
                    print("Last call cost")
                case 2: 
                    print("All calls' cost")
                case 3: 
                    print("Clear counters")
                case 0: 
                    print("Invalid options")

        case 7: 
            print("""
Callcostsettings
1 Call cost limit
2 Show costs in
""")

            callcostssettings_choice = int(input())
            match callcostssettings_choice:
                case 1: 
                    print("Call cost limit")
                case 2: 
                    print("Show costs in")
                case 0: 
                    print("Invalid options")

        case 8: 
            print("Prepaid credit ")
        case 0: 
            print("Invalid options")

def Tones():
    print("""
Tonesmenu

1 Ringing tone
2 Ringing volume
3 Incoming call alert
4 Message alert tone
5 Keypad tones
6 Warning tones
7 Vibrating alert
8 Screen saver
                                                    
""")
    choice = int(input())

    match choice:
        case 1: 
            print("Ringing tone")
        case 2: 
            print("Ringing volume")
        case 3: 
            print("Incoming call alert")
        case 4: 
            print("Message alert tone")
        case 5: 
            print("Keypad tones")
        case 6: 
            print("Warning tones")
        case 7: 
            print("Vibrating alert")
        case 8: 
            print("Screen saver")
        case 0: 
            print("Invalid options")

def Settings():
    print("""
Settingsmenu

1 Call settings
2 Phone settings
3 Security settings
4 Restore factory settings                                                   
""")
    choice = int(input())

    match choice:
        case 1: 
            print("""
Callsettings
1 Automatic redial
2 Speed dialing
3 Call waiting options 
4 Own number sending
5 Phone line in use
6 Automatic answer
""")
            callsettings_choice = int(input())
            match callsettings_choice:
                case 1: 
                    print("Automatic redial")
                case 2: 
                    print("Speed dialing")
                case 3: 
                    print("Call waiting options")
                case 4: 
                    print("Own number sending")
                case 5: 
                    print("Phone line in use")
                case 6: 
                    print("Automatic answer")
                case 0:
                    print("Invalid options")

        case 2:
            print("""
Phonesettings
1 Language
2 Cell info display
3 Welcome note
4 Network selection
5 Confirm SIM service actions
""")

            phonesettings_choice = int(input())
            match phonesettings_choice:
                case 1: 
                    print("Language")
                case 2: 
                    print("Cell info display")
                case 3: 
                    print("Welcome note")
                case 4: 
                    print("Network selection")
                case 5: 
                    print("Confirm SIM service actions")
                case 0: 
                    print("Invalid options")

        case 3:
            print("""
Securitysettings
1 PIN code request
2 Call barring service
3 Fixed dailing 
4 Closed user group
5 Security level
6 Change access codes
""")

            securitysettings_choice = int(input())
            match securitysettings_choice:
                case 1: 
                    print("PIN code request")
                case 2: 
                    print("Call barring service")
                case 3: 
                    print("Fixed dailing ")
                case 4: 
                    print("Closed user group")
                case 5: 
                    print("Security level")
                case 6: 
                    print("Change access codes")
                case 0: 
                    print("Invalid options")

        case 4: 
            print("Restore factory settings")
        case 0: 
            print("Invalid options")

def Music():
    print("""
Musicrmenu

1 Music player
2 Radio
3 Recorder
4 Track list                    
""")
    choice = int(input())

    match choice:
        case 1: 
            print("Music player")
        case 2: 
            print("Radio")
        case 3: 
            print("Recorder")
        case 4: 
            print("Track list")
        case 0: 
            print("Invalid options")

def Clock():
    print("""
Clockrmenu

1 Alarm clock
2 Clock settings
3 Date settings
4 Stop watch
5 Countdown timer
6 Auto update of date and time               
""")
    choice = int(input())

    match choice:
        case 1: 
            print("Alarm clock")
        case 2: 
            print("Clock settings")
        case 3: 
            print("Date settings")
        case 4: 
            print("Stop watch")
        case 5: 
            print("Countdown timer")
        case 6: 
            print("Auto update of date and time")
        case 0: 
            print("Invalid options")

main() 











