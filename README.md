# dropengine
Malleable payload generation framework.

By [@s0lst1c3](https://twitter.com/s0lst1c3)

# Install

Clone the git repo:
```
git clone https://github.com/s0lst1c3/dropengine.git
```

Create a new virtual env:
```
python3.7 -m venv venv 
```

Activate the virtual env:

```
source venv/bin/activate
```

# Constructing a Basic Payload

## Module Selection

DropEngine accepts a list of module names from the command line and uses them to construct a payload. To make things a bit easier to follow, this guide will walk you through the process of listing the various types of modules needed to create a basic payload. Keep in mind that we're not actually executing anything yet. We're just seeing what modules are available and describing what they do.

First, we need to decide what kind of shellcode runner we want to use. To get a list of available shellcode runners, use the `--list runners` flag:

Command:
```
python dropengine.py --list runners
```

Example Output:

```
(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ python dropengine.py --list runners

Listing runners:

    runner - basic_csharp_runner
    runner - basic_csharp_runner_no_mutation
    runner - csharp_installutil
    runner - msbuild_csharp_runner

(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ 
```

We'll go ahead and plan to use the "msbuild_csharp_runner", which will give us an MSBuild payload written in C#.

Next, we'll need to select an interface module that is compatible with our shellcode runner. In DropEngine, you can think of interfaces as the "glue" that binds your payload together. The interface facilitates communication between you (the user), and between the various modules in your payload. 

To get a list of available interfaces, use the `--list interfaces` flag as shown in the following example:

Command:
```
python dropengine.py --list interfaces
```

Example Output:
```
(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ python dropengine.py --list interfaces

Listing interfaces:

    runner_interface - csharp_runner_interface - Interface for generating CSharp payloads
```

As you can see from the Example Output shown above, the only available interface at this time is the csharp_runner_interface, which is designed for building payloads using C#.

Next, let's decide on a crypter to protect our shellcode. To obtain a list of available crypters, use the `--list crypters` flag as shown below:

Command:
```
python dropengine.py --list crypters
```

Example Output:
```
(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ python dropengine.py --list crypters 

Listing crypters:

    crypter - crypter_aes

(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ 

```

As with our interfaces, we really only have one crypter module available at this time, and that's "crypter_aes".

We'll also need a decrypter module to convert our shellcode back into plaintext. To get a list of decrypters, use the `--list decrypters` command:

Command:
```
decrypter - decrypter_csharp_rijndael_aes
```

Example Output:
```
(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ python dropengine.py --list decrypters

Listing decrypters:

    decrypter - decrypter_csharp_rijndael_aes

(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ 
```

We'll go ahead and use the "decrypter_csharp_rijndael_aes", since it's compatible with our crypter module.

Now we need to select encryption and decryption key modules to use with our selected crypter and decrypter. To list all available crypters and decrypters, use the `--list ekeys dkeys` command as shown below:

Command:
```
 python dropengine.py --list ekeys dkeys
```

Example Output:
```
(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ python dropengine.py --list ekeys dkeys

Listing ekeys:

    ekey - ekey_env_ad_domain_name       
    ekey - ekey_env_ext_fqdn
    ekey - ekey_env_ext_ip
    ekey - ekey_env_hd_serial
    ekey - ekey_env_int_fqdn
    ekey - ekey_env_int_hostname
    ekey - ekey_env_mac_addr
    ekey - ekey_env_mac_oui
    ekey - ekey_env_moonphase
    ekey - ekey_env_timezone
    ekey - ekey_env_username
    ekey - ekey_env_vol_serial
    ekey - ekey_one_time_remote_http     
    ekey - ekey_static

Listing dkeys:

    dkey - dkey_csharp_static
    dkey - dkey_csharp_env_ad_domain_name
    dkey - dkey_env_csharp_ext_fqdn      
    dkey - dkey_env_csharp_ext_ip        
    dkey - dkey_env_csharp_hd_serial     
    dkey - dkey_env_csharp_int_fqdn      
    dkey - dkey_env_csharp_int_hostname  
    dkey - dkey_env_csharp_mac_addr      
    dkey - dkey_env_csharp_mac_oui       
    dkey - dkey_env_csharp_moonphase     
    dkey - dkey_env_csharp_timezone      
    dkey - dkey_env_csharp_username      
    dkey - dkey_env_csharp_vol_serial    
    dkey - dkey_remote_csharp_otk_http   

(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ 
```

Let's keep things simple for now and use the two static key modules: "dkey_csharp_static" and "ekey_static".

Next, we need to select an executor module to execute our raw shellcode. To get a list of available executors:

Command:
```
python dropengine.py --list executors
```

Example Output:
```
(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ python dropengine.py --list executors

Listing executors:

    executor - executor_csharp_virtual_alloc_thread

(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ 
```

At this time, our only compatible executor is "executor_csharp_virtual_alloc_thread", so we'll use that.

Finally, we just need to select a mutator module to perform symbol transformation on our completed payload. To get a list of available mutators, use the `--list mutators` command:

Command:
```
python dropengine.py --list mutators
```

Example Output:
```
(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ python dropengine.py --list mutators

Listing mutators:

    mutator - mutator_null
    mutator - mutator_random_string
    mutator - mutator_rot13
    mutator - mutator_wordlist

(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ 
```

We'll go ahead and use the "mutator_random_string" module.

Select a runne here

## Creating the Payload

We've now explored the various payload components available to us and selected the ones we want to use. Now it's time to create our payload. Recall that in the previous section we made the following sections:
- interface - csharp_runner_interface
- crypter - crypter_aes
- decrypter - decrypter_csharp_rijndael_aes
- encryption key - ekey_static
- decryption key - dkey_csharp_static
- executor - executor_csharp_virtual_alloc_thread
- mutator mutator_random_string

To run DropEngine with these selections, use the following command (note that the --shellcode flag should point to your shellcode, and the -o flag will specify the output path):

```
(venv) s0lst1c3@DESKTOP-NC0U49D:/mnt/c/Users/s0lst1c3/obfuscation$ python dropengine.py --interface csharp_runner_interface \
--crypter crypter_aes \
--decrypter decrypter_csharp_rijndael_aes \
--ekey ekey_static \
--runner msbuild_csharp_runner \
--dkey dkey_csharp_static \
--executor executor_csharp_virtual_alloc_thread \
--mutator mutator_random_string \
--shellcode shell.bin \
--o example.csproj
```

