# netlogo-swarmathon-competition-script
Teams participating in the 2017 Swarmathon High School Division can use this script to validate their code and check for illegal commands and other rules violations. This script is not meant to be a direct substitute for precise following of the rules outlined in BC-Lab-UNM/netlogo-swarmathon. Please be sure to review the rules and complete the checklist found in [Sw5] prior to submitting your competition code. <br><br>
This script was written in Python 2.7x and Java 1.8x on macOS Sierra. It has not been tested on other versions of Python, Java, or Linux or Windows. The included bash script is tailored specifically for use with macOS and modifications will need to be made to run it in Linux or Windows.<br><br>
<b><u>contents</b></u><br>
<ul>
<li></li>
</ul><br>
<b><u>requirements</b></u><br>
<ul>
<li>Python 2.7x</li>
<li>The py4j library; install directions at https://www.py4j.org/ </li>
<li>The JDK (Java Development Kit); install directions at https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html</li>
OPTIONAL<br>
<li>A plain text editor to edit your launcher script</li>
</ul><br>
<b><u>how to use it</b></u><br>
These instructions assume macOS.<br>
<ul>
<li>Place your Netlogo file in the same directory as the script files.</li>
<li>Open 2 Terminal windows.</li>
<li>Navigate to the directory where the script files and your source .nlogo file are located in both Terminal windows.</li>
<li>In Terminal 1, enter <code>./osxlancher.sh </code> </li>
<li>The message <code>Server running</code> should appear in your Terminal 1 window.</li>
<li>Move to Terminal 2. Enter <code>python HSDivisionTeamValidationScript.py test.nlogo</code><br>
You should see this generated dialogue appear in the terminal: </li></ul><br>
<code>
This script checks for rules violations in your program.
If you are unclear on the rules, please review them in [Sw5].

Openingtest.nlogo.

Your file is named incorrectly.<br><br>

Testing setup functions...<br><br>

Test for exactly 6 robots: <br>
6.0<br>
OK<br><br>

Test for robots spawning at origin.<br><br>

6.0 robots were not spawned at (0, 0).<br>
WARNING! All 6 robots must begin at (0,0).<br><br>


Test world size.<br><br>

OK<br><br>

Checking for illegal commands...

move-to
WARNING! Illegal command move-to found.

setxy
WARNING! Illegal command setxy found.

hatch
WARNING! Illegal command hatch found.

die
WARNING! Illegal command die found.

sprout
WARNING! Illegal command sprout found.

Running program for 3600 ticks.

Complete.
</code>

