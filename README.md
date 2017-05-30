# netlogo-swarmathon-competition-script
Teams participating in the 2018 Swarmathon High School Division can use this script to validate their code and check for illegal commands and other rules violations. This script is not meant to be a direct substitute for precise following of the rules outlined in BC-Lab-UNM/netlogo-swarmathon. Please be sure to review the rules and complete the checklist found in [Sw5] prior to submitting your competition code. <br><br>
There are two versions of the script written in Python and Java 1.8x, utlizing the NetLogo Bridge framework derived from https://github.com/dmasad/Py2NetLogo. One version is written in Python 2.7x and the other is written in Python 3.6x. There are also launcher scripts for both Windows and Mac OS X. Neither other versions of Python nor other operating systems have been tested with these scripts. <br>

<b><u>Contents</b></u><br>
<ul>
<li>HSDivisionTeamValidationScript.py</li>
<li>HSDivisionTeamValidationScript_P3.py</li>
<li>NetLogoBridge.java</li>
<li>README.md</li>
<li>osxlauncher.sh</li>
<li>parkinglot.jpg</li>
<li>test.nlogo</li>
<li>winlauncher.bat</li>
</ul><br>
<b><u>Requirements</b></u><br>
<ul>
<li>Python 2.7x or Python 3.6x</li>
<li>The py4j library; install directions at https://www.py4j.org/ </li>
<li>The JDK (Java Development Kit); install directions at https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html</li>
OPTIONAL<br>
<li>A plain text editor to edit your launcher script</li>
</ul><br>
<b><u>Mac OS X Instructions</b></u><br>
<ul>
<li>Locate the <code>py4j</code> and the <code>Netlogo</code> .jar files.</li>
<li>Modify the <code>./osxlauncher.sh</code> script. Change the script to reflect the path to the jar files on your computer. Separate the paths with a colon. We recommend simplifying path names by renaming Netlogo 5.2 to Netlogo5.2 and the script reflects this.</li>
<li>If you are using Python 2.7x, make sure the <code>osxlauncher.sh</code> script references <code>HSDivisionTeamValidationScript.py</code>. If you're using Python 3.6x, reference <code>HSDivisionTeamValidationScript_P3.py</code> instead.</li>
<li>Place your Netlogo file in the same directory as the script files.</li>
<li>Open 2 Terminal windows.</li>
<li>Navigate to the directory where the script files and your source .nlogo file are located in both Terminal windows.</li>
<li>In Terminal 1, enter <code>./osxlauncher.sh </code> </li>
<li>The message <code>Server running</code> should appear in your Terminal 1 window.</li>
<li>Move to Terminal 2. Test your installation of the script by entering <code>python HSDivisionTeamValidationScript.py test.nlogo</code><br>
You should see a generated dialogue appear in the terminal that starts with: </li></ul><br>
<code>
This script checks for rules violations in your program.<br>
If you are unclear on the rules, please review them in [Sw5].<br></code>

and ends with<br>

<code>
Complete.<br>
</code>
<br>
<ul>
<li>Now test your .nlogo file by replacing <code>test.nlogo</code> with <i><code>yourFileName</i>.nlogo</code></li><br>

<b><u>Windows Instructions</u></b><br>
<ul>
<li>Locate the <code>py4j</code> and the <code>Netlogo</code> .jar files.</li>
<li>Modify the <code>winlauncher.bat</code> file. Change the file to reflect the path to the jar files on your computer. Separate the paths with a semicolon.</li>
<li>If you are using Python 2.7x, make sure the <code>winlauncher.bat</code> file references <code>HSDivisionTeamValidationScript.py</code>. If you're using Python 3.6x, reference <code>HSDivisionTeamValidationScript_P3.py</code> instead.</li>
<li>Double-click on the <code>winlauncher.bat</code> file to execute the validation script; two Command Prompt windows will automatically launch and execute commands.</li>
<li>The message <code>Server running</code> should appear in the first Command Prompt.</li>
<li>You should see a generated dialogue appear in the second Command Prompt that starts with: </li></ul><br>
<code>
This script checks for rules violations in your program.<br>
If you are unclear on the rules, please review them in [Sw5].<br></code>

and ends with<br>

<code>
Complete.<br>
</code>
<br>
<ul>
<li>Now test your .nlogo file by replacing <code>test.nlogo</code> with <i><code>yourFileName</i>.nlogo</code></li><br>
