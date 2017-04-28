# OfficeSpaceAllocation
**Introduction:**
> This is a simple commandline application that was developed by Simon Peter Ssekamatte for the Andela Uganda Cohort I bootcamp as the final requirement for the Andela Felowship selection process. OfficeSpaceAllocator is a commandline application that allows the user to create rooms in an Andela Facility called The Dojo and allocate people to those rooms.

**Proposed Application Functionalities:**
- [x] Create rooms*
- [x] Add people to the rooms*
- [x] Print room allocations
- [ ] Reallocate people
- [ ] Save and retrieve in a database

**User Guide**
- Clone/download a version of the app to local machine
- Install the virtual environment to the root folder with the command: pip install virtualenv`
- Activate the virtual environment by navigating to its scripts and running the `activate.bat` file
- Install the app required libraries by running the command: `pip install -r requirements.txt`
- Run the *doc_opt.py* file from the *app* folder appending the tag `-i` at the end of the run command
- When the file successfully runs, use the commands `create_room <room_type> <room_name>...` to create a room and `add_person <person_name> <FELLOW|STAFF> [wants_accommodation]` to add a person
