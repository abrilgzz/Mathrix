INIT:

- Install XAMPP
- Install Python 3
- Modify Apache server config

  > ADD FOLLOWING LINES AT END OF httpd.conf
  >
  > ```
  > AddHandler cgi-script .py
  > ScriptInterpreterSource Registry-Strict
  > ```

  > Moddify IfModule dir_module
  >
  > ```
  > <IfModule dir_module>
  >   DirectoryIndex index.php index.pl index.cgi index.asp index.shtml index.html >index.htm \
  >   default.php default.pl default.cgi default.asp default.shtml default.html >default.htm \
  >   home.php home.pl home.cgi home.asp home.shtml home.html home.htm index.py
  > </IfModule>
  > ```

- `$ sudo pip install numpy scipy`
- `$ sudo pip install fastnumbers`

# Run

To run files on server please start the apache server on XAMPP then open any .py file on the following url:
`http://localhost/python/mathrix/server/`
