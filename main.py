from bmi_calc import bmi_check

# Call the bmi_calc function and add in a user interface for the bmi calculator (ex. welcome message, instructions, etc.)

# Add your code here
while True:
    print('''                                                                                                                        
                                                           .*/#%%%%%%%%%%%%#(*.                                                 
                                                 ,/##*. .*/*,.              .,*/*.  ,(%/.                                       
                                            *%/ ./,   *#%%%%%%%%%%%%%%%%%%%%%%%%%%%/.  ,/. ,%(,                                 
                                       .%/ **  ,%%%%%%%%##%%%%%%%%%%% %%# *#%(  #%##%%%%%&(  ,/ .%*                             
                                    %/ /  .&%%%%%#/ ,##( #%%%%%%%%%%# #%# (%%/ . #, (%#  (%%%%&/  ( .%*                         
                                .%.,* .%%%%%#**%%%&* * /, #%%%%%%%%%# ### #%# /# * (%%/ #%%#  #%%%&/ ,, #*                      
                              %.,, /%%%%%%%# ,  #%%% .##.  (%%%%%%%%%%%%%%%%%#(%#  #(/ #%%%, %%/  #%%%% .* #,                   
                           /( / *%%%%#  %%%%( ./#  (((#%%%%%&%/,.          .*#%&%%%%%%#%%%% #  #%%%# ,#%%# , ,%                 
                         #,,  &%%%%( #%%%%#%#  (%%%%%%,                              #%%%%%# (%%%#  %&% /%%&. * &.              
                       (,*  &%%%*.#%%  #%# (%%%%%,                  /((                   #%%%%(  ##.#%%%# #%%/ / %             
                     */.  &%%%%%%( .#%#,,#%%%/                     (((((                     .%%%%* #%%/ .#( #%%* *.%           
                    % / %%%%,  .#%%%/ (%%%/      #                 (. .(                 *(      %%%#  #%/   #%%%& , (.         
                  */, .%%%# .#( #   #%%%      ((((((#                                 ,((((((,     (%%%/  #%%#/,#%%# * #        
                 ( / #%%%%%%%#  ((%%%%         /((((                                   .((((         /%%#% /# #%#.#%& ( &       
                % ( &%%% #%#%%%#/%%%                                                                   #%%.*%( ##/%%%% * #      
               # * %%%#  .(.(%,*%%(                                                                      %%#(#%%%#* #%%,, %     
              /,# &%%#%%%%%#. #%%,%%%#*/%%(*                                                   .*#%(/%%%%/&%#  ,##%%%&%& * %    
             .(, /%%%.    ,(.#%%    *((//(&&&%(*%&.                                     (&//%&%&%%(#((,#   #%%%%%%%%(.%%& (,(   
             % , &%%%%%( /%#(%%,   .(%%%%%%(&%%###%%%%%             .               *&%%&%%%&%%#%###(*%/    &%,,.     #%%(  %.  
            ,/* %%%#.  /(%%%%%(      /&&%%%%%%#%%%%%*%%%&     .%%%%%./*&%%/       %%%%(####(/###(((#%#(.     &(#%%%%%*/#%& * (  
            #./ &%%%%%%#(/ *&%         .%%#%%%%*%(*#&%%%%*    #  /%%%%%%%%#      *%%%%#%%(#/&###(/%/         (%%%%%%%%(#%%*, %  
            &  ,%%%%%%%%## (%(          ,////((%%%%&/%%%.         .&%%%%%%&        &%&,&%%&#&%&&&&&*         .%%%%%%(  /%%%  (  
            %. *%%%*  ./ ###%*          *%%&&&%#&%%#%%%&         &%%%%%%%%%%       &%%%(#%%(&%%%%%%/          &/     #%%%%& ,*, 
           ,%. /%%%(((*    (%,           #%%%%%(####&(%%&.(,/,       %%%%%%%%#** .&%&(%&%##/%%&%%&            &%%%%%%/ /%%& ,*, 
            &. *%%%%%%%%%%%%%*             ,%%###%(&&##%%%,   &  %   %######%#%*%%&%#%%%(&%%(#%%              &%%%%%%%%%%%& ./* 
            % ,.%%%%%%%#%%%%%#                /#%%&##%&%%%,  # #%,(  %######%#%*&%#%&%#(&%%%,*               .%%%%%%%%%%%%#. #  
            *,( &%%%%#(((#%%%&                  %%%%#%##%%, (.&((/*, %######%#%*&#%%/%&#%%(.                 #%%%##((##%%% * #  
             #  *%%%%#((((%%%%#                   &%(%%(%#,(##%,###%,%%%####%%%*%#%#%&*&&                    %%%%%((((%%%% ,*,  
             (./ %%%%#%%%%%%%%%,                    (/&&/%.%######%%% .......  *%&(%&/&                     &%%%%#%%%%%%%,/ &   
              & ..%%%%%%%%%%%%%%          ,              ,.%##%###%#% %% %%% % *,.,                        %%%%%%%%%%%%%#. (    
               #  ,%%%%%%%%%%%%%%,       /,*            .&.%%#%###%#%  % %%# % *%&             //*        &%%%%%%%%%%%%% ,*#    
               .#, *%%%%%%%%%%%%%%%       /, .        /%%%.%##%##%%%% *% %,    *%%%%/     #&../         .%%%%%%%%%%%%%& *,/     
                .# ..%%%%%%%%%%%%%%%.      %# %%%. ./%%%%% %#####%%%% #####   /,%%%%%%%###%& . %,      %%%%%%%%%%%%%%# ,,/      
                  % , &%%%%%%%%%%%%%%%     ((##/%%(#*(&&&&%, *#*/%%%%   //*(*  ,#&&&&&#.. %* /#/     (%%%%%%%%%%%%%%/. (*       
                   # / #%%%%%%%%%%%%%%%%     /&#/                *%%%%%%%#               (,, .     %%%%%%%%%%%%%%%& # &         
                    ,# , &%%%%%%%%%%%%%%%%%       (            ,%%%%%%%%%%%*              #(    ,%%%%%%%%%%%%%%%%* .*/          
                      /*...&%%%%%%%%%%# *%%%%#                &%%%%%%%%%%%%%&                *&%%# #%%%%%%%%%%%( * #            
                        #*,. &%%%%%%# .%%,.%%%%%%(           (#/%%%%%%%%%%%%(#           ,%%%%# #%# .%%%%%%%%/ * %              
                          // * %%%#, #%###&/ #%/%%%%%%#          .%%%%#&%,/(        *%%%%%%, /%#  (%#  (%%&....%                
                            ,% / .&%%%%%%% ,  * ##  #%%%%%%%%&%(*.       .,(%&%%%%%%#((/   ((. %%%  %%%%( # #/                  
                               /# ( .%%%%#.%# *%&* ./% ,#( .*(%%%%%%%%%%%%%##/*.(#, #%(%&/ (#,  ,%%%%/ / *%.                    
                                  /# *, /&%%%#%#* #( ..%# #%# ##  (%#  #%%%% ,%# (%, ##%#%( *#%%%# ./ /#                        
                                     .%/ ** .%%%%%%#  #% ,%%..%# (* ,( #%%%%# #%%%%#  *(%%%%&/ ./ ,%*                           
                                          #%  /*  *&%%%%%%###%%, .%#%. *&%%%#*(#%%%%%%&#  .(  #%*                               
                                               /%(. ,/*   ./#%%%%%%%%%%%%%%%%#(,   ,(,  /%(.                                    
                                                      ,(%#(,.    .,,,,,,..   .,/#%(/.                                          ''')
    print('''\n\n

    ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║   ,---.  ,--. ,--.,------. ,------.     ,-----.  ,--.   ,--.,--.     ,-----.        ,--.              ,--.          ,--.                  ║
    ║  /  O  \ |  | |  ||  .--. '|  .--. '    |  |) /_ |   `.'   ||  |    '  .--./ ,--,--.|  | ,---.,--.,--.|  | ,--,--.,-'  '-. ,---. ,--.--.  ║
    ║ |  .-.  ||  | |  ||  '--' ||  '--' |    |  .-.  \|  |'.'|  ||  |    |  |    ' ,-.  ||  || .--'|  ||  ||  |' ,-.  |'-.  .-'| .-. ||  .--'  ║
    ║ |  | |  |'  '-'  '|  | --' |  | --'     |  '--' /|  |   |  ||  |    '  '--'\\\ '-'  ||  |\ `--.'  ''  '|  |\ '-'  |  |  |  ' '-' '|  |     ║
    ║ `--' `--' `-----' `--'     `--'         `------' `--'   `--'`--'     `-----' `--`--'`--' `---' `----' `--' `--`--'  `--'   `---' `--'     ║
    ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
            ''')

    print("    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                                                    ⚖️  Welcome to AUPP BMI Calculator ⚖️                                                       ")
    print("    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    
    #Initialize variables to store user's inputs
    userNameInfo = input("\t🧾 Please enter your name: ")
    userWeight = input ("\t⚖️ Please Enter your Weight in (KG): ")
    userHeight = input ("\t🌴 Enter your Height in (Meter): ")

    #Create two variable to store the values since the function return 2 values
    result1, result2 = bmi_check(userWeight, userHeight)
    print("\n    ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("    ║                                                                                                                                           ║")
    print(f"    ║\t\tGood day Mr/Mrs {userNameInfo} your weight is {result1} and your BMI is {result2}                                                                  ║")
    print("    ║                                                                                                                                           ║")
    print("    ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    
    more_try = input("\n\tDo you want to continue? (Y/N): ")
    if (more_try.upper() == "Y"): 
        continue
    else: 
        print('''\n
    ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║     _____ _                 _       __                        _                                     _    ____  ____                       ║
    ║    |_   _| |__   __ _ _ __ | | __  / _| ___  _ __   _   _ ___(_)_ __   __ _    ___  _   _ _ __     / \  |  _ \|  _ \                      ║
    ║      | | | '_ \ / _` | '_ \| |/ / | |_ / _ \| '__| | | | / __| | '_ \ / _` |  / _ \| | | | '__|   / _ \ | |_) | |_) |                     ║
    ║      | | | | | | (_| | | | |   <  |  _| (_) | |    | |_| \__ \ | | | | (_| | | (_) | |_| | |     / ___ \|  __/|  __/                      ║
    ║      |_| |_| |_|\__,_|_| |_|_|\_\ |_|  \___/|_|     \__,_|___/_|_| |_|\__, |  \___/ \__,_|_|    /_/   \_\_|   |_|                         ║
    ║                                                                       |___/                                                               ║
    ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
''')
        break