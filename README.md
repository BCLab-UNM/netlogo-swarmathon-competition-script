# netlogo-swarmathon-competition-script
Teams participating in the 2017 Swarmathon High School Division can use this script to validate their code and check for illegal commands and other rules violations. This script is not meant to be a direct substitute for precise following of the rules outlined in BC-Lab-UNM/netlogo-swarmathon. Please be sure to review the rules and complete the checklist found in [Sw5] prior to submitting your competition code. <br><br>
This script was written in Python 2.7x and Java 1.8x on macOS Sierra. The NetLogo Bridge framework is derived from https://github.com/dmasad/Py2NetLogo, to which I have made some contributions. It has not been tested on other versions of Python, Java, or Linux or Windows. The included bash script is tailored specifically for use with macOS and modifications will need to be made to run it in Linux or Windows.<br><br>
<b><u>contents</b></u><br>
<ul>
<li>HSDivisionTeamValidationScript.py</li>
<li>NetLogoBridge.java</li>
<li>README.md</li>
<li>osxlauncher.sh</li>
<li>parkinglot.jpg</li>
<li>test.nlogo</li>
</ul><br>
<b><u>requirements</b></u><br>
<ul>
<li>Python 2.7x</li>
<li>The py4j library; install directions at https://www.py4j.org/ </li>
<li>The JDK (Java Development Kit); install directions at https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html</li>
OPTIONAL<br>
<li>A plain text editor to edit your launcher script</li>
</ul><br>
<b><u>how to use it: macOS</b></u><br>
<ul>
<li>Locate the <code>py4j</code> and the <code>Netlogo</code> .jar files.</li>
<li>Modify the <code>./osxlauncher.sh</code> script. Change the script to reflect the path to the jar files on your computer. Separate the paths with a colon. I renamed Netlogo 5.2 to Netlogo5.2 and the script reflects this; you may want to do the same.</li>
<li>Place your Netlogo file in the same directory as the script files.</li>
<li>Open 2 Terminal windows.</li>
<li>Navigate to the directory where the script files and your source .nlogo file are located in both Terminal windows.</li>
<li>In Terminal 1, enter <code>./osxlauncher.sh </code> </li>
<li>The message <code>Server running</code> should appear in your Terminal 1 window.</li>
<li>Move to Terminal 2. Test your installation of the script by entering <code>python HSDivisionTeamValidationScript.py test.nlogo</code><br>
You should see this generated dialogue appear in the terminal that starts with: </li></ul><br>
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
<b><u>how to use it: Windows and Linux</u></b><br>
Follow the instructions as per macOS, except:<br> 
<ul>
<li>either modify the launcher script</li>
<li>or compile the Java file manually, using the <code>javac</code> command with the CLASSPATH as an argument</li>

