![DropEngine](https://raw.githubusercontent.com/s0lst1c3/dropengine/master/DropEngine%201.png)

By [@s0lst1c3](https://twitter.com/s0lst1c3)

# Overview

Defense Evasion techniques tend to have a short shelf-life, and this is especially true for techniques used during initial access. Because of this, initial access payloads are often prepared on a per-engagement  basis, which can be time-consuming when payloads are created entirely by hand. DropEngine addresses this problem by providing a malleable framework for creating shellcode runners, allowing operators to choose from a selection of components and combine them to create highly sophisticated payloads within seconds.

Available payload components include crypters, execution and injection mechanisms, as well as environmental nad remote keying functions. Also included are pre-execution modules such as sandbox checks and AMSI bypasses. Although these pre-packaged example modules may prove useful, DropEngine's true strength is in its ability to improve operational efficiency by providing a high degree of payload standardization while simultaneously allowing operators to control just about every aspect of the payload's signature and behavior.

# Disclaimer

DropEngine (the "Software") and associated documentation is provided “AS IS”. The Developer makes no other warranties, express or implied, and hereby disclaims all implied warranties, including any warranty of merchantability and warranty of fitness for a particular purpose. Any actions or activities related to the use of the Software are the sole responsibility of the end user. The Developer will not be held responsible in the event that any criminal charges are brought against any individuals using or misusing the Software. It is up to the end user to use the Software in an authorized manner and to ensure that their use complies with all applicable laws and regulations.

# Documentation

All documentation is available on the project's Wiki, which can be found here: https://github.com/s0lst1c3/dropengine/wiki

# Acknowledgments
This tool either builds upon, is inspired by, or directly incorporates nearly ten years of prior research and development from the following awesome people:

* [@subtee](https://twitter.com/subtee)
* [secretsquirrel](https://github.com/secretsquirrel)
* [Antonio24](https://github.com/antonio24)
* [matterpreter](https://github.com/matterpreter)
* [dmchell](https://github.com/dmchell)
* [leoloobeek](https://github.com/leoloobeek) 
* [Chris Truncer](https://twitter.com/christruncer)
* [Harmj0y](https://github.com/harmj0y)
* [byt3bl33d3r](https://github.com/byt3bl33d3r)
* [arvanaghi](https://github.com/arvanaghi)

This list will likely grow as additional functionality is added to the project.

For a complete description of what each of these people has contributed to the current payload development landscape and this tool, please see:

* [https://github.com/s0lst1c3/dropengine/wiki/Acknowledgements](https://github.com/s0lst1c3/dropengine/wiki/Acknowledgements)
