Here's a stupid little python mockup of a personal utility app I've been wanting to write. In the end, I want to write it so I have a bit of experience with app dev for android, and it's just a tool I've been wanting to keep track of my homework assignments. 

To use the mockup, enter "python organizerUI.py" into the terminal and enjoy.



Below are my notes: 
Basic idea:
    - Keep a bunch of assignments in a priority queue 
    - When asked, display assignments in order of due date

What I need:
    - API:
        - Add assignments
        - organize assignments
            - Start just by organizing by due date, eventually organize by more things
        - Remove assignments
            - Should auto-remove if past due date
                - Maybe eventually verify that they've been finished or whatever
            - Need to keep a hash-type value of every assignment so I know which one to remove. This also means either not always using a PQueue, or adding a lazy remove method to my existing PQueue. Could just hash by title and require unique titles. 

    -UI:
        - Don't work too hard on this, this is just a mockup
        - For now, just display assignments when asked to, give way to add


API:
    - Assignment class:
        - Stores assignment data
        - Compares dates
        - Start with init only, then possibly add ability to edit

    - Organizer class:
        - Stores assignments
        - returns organized array for UI usage
