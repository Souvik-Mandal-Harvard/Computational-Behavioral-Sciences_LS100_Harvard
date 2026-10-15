---
subtitle: 'LS100 — Module 01A · Video Data'
title: Make Your Own Computer Vision Camera Using Raspberry Pi
short_title: 'Guide 02: Make a video camera'
exports:
  - format: pdf
    template: lapreprint-typst
    output: exports/LS100_module-01A_Video-Data_content-00_Guide-02_Make-Your-Own-Computer-Vision-Camera-Using-Raspberry-Pi_LastUpdated-20260726.pdf
    id: pi-camera-pdf
downloads:
  - id: pi-camera-pdf
    title: Download the article (PDF)
---

*Authored by* **Souvik Mandal, Ph.D.**

*Project Leader & Instructor, Computational Behavioral Sciences, LS100, FAS, Harvard University* | Linkedin ID: [souvik-mandal-phd](https://www.linkedin.com/in/souvik-mandal-phd)

---

## Introduction: From Small Computer to Research Camera

A computer vision camera is not only a lens pointed at the world. It is a complete system that records visual data, stores it, and often begins analyzing it immediately. Raspberry Pi makes this idea accessible because it combines a small Linux computer, a camera interface, Python support, and flexible hardware input and output in a format that is inexpensive, portable, and easy to reconfigure.

For behavioral sciences, this makes Raspberry Pi especially attractive. A Raspberry Pi camera system can be mounted near a bird feeder, placed beside an animal arena, attached to a tripod in a classroom, or integrated into a custom enclosure for long-term observation. It can act as a recorder, a networked field device, or the front end of a computer vision pipeline.

This guide introduces the logic of choosing the right Raspberry Pi and the right camera for a behavioral research task. The most important question is not simply which hardware is most powerful. It is which combination preserves the information your study needs.

## What Is a Raspberry Pi?

Raspberry Pi is a family of compact single-board computers. Unlike a microcontroller, which is usually designed for simple control tasks, a Raspberry Pi runs a full operating system, supports Python and other programming languages, can store files, connect to networks, and run computer vision software directly.

Several features make Raspberry Pi useful for behavioral video work:

  - It runs Linux, which makes it well suited for scripting, automation, and remote access.

  - It supports Python libraries commonly used in image and video analysis.

  - It includes a CSI camera interface for direct connection to official Raspberry Pi camera modules.

  - It can be deployed as a lightweight, dedicated recording system rather than as a full desktop computer.

  - It can interact with other hardware such as infrared lights, sensors, storage devices, and network services.

In other words, Raspberry Pi is not just a camera controller. It can be the small computer at the center of an entire visual data collection system.

## Which Raspberry Pi Computer Should You Choose?

Before choosing a camera module, it helps to choose the Raspberry Pi computer itself. All official Raspberry Pi cameras work with Raspberry Pi computers that have CSI camera connectors, but the boards differ substantially in computing power, connector type, thermal behavior, and how suitable they are for local computer vision processing.

| **Raspberry Pi Computer** | **Camera Connector Situation** | **Strengths** | **Best Use Cases** | **Main Limitations** |
| --- | --- | --- | --- | --- |
| **Raspberry Pi Zero 2 W** | One mini 22-pin CSI connector | Very small, low power, inexpensive, easy to hide in compact spaces | Lightweight recording at a feeder, small remote observation rigs, simple streaming or capture tasks | Limited RAM and processing power; not ideal for demanding on-device computer vision |
| **Raspberry Pi 4 Model B** | One standard 15-pin CSI connector | Mature platform, more power than Zero 2 W, good for recording and moderate processing | General-purpose recording, classroom prototypes, remote monitoring, light computer vision workflows | Only one camera connector; less headroom than Pi 5 for heavy local inference |
| **Raspberry Pi 5** | Two mini 22-pin camera/display connectors | Highest processing power, dual camera support, best choice for demanding local workflows | On-device computer vision, higher-throughput capture, multi-camera experiments, real-time processing | Higher power draw; often benefits from active cooling |
| **Compute Module 4** | Camera support depends on carrier or IO board, commonly with two mini 22-pin connectors | Strong embedded flexibility, good for custom enclosures and product-like builds | Custom camera housings, permanent installations, integrated field devices, dual-camera embedded rigs | More setup complexity than standard Raspberry Pi boards |

Two practical points matter immediately. First, Raspberry Pi 4 uses the larger 15-pin camera connector, whereas Raspberry Pi 5, Raspberry Pi Zero boards, and Compute Module IO boards use the smaller 22-pin connector. Second, even if a camera is electrically compatible, the board may not be equally suitable for the computational workload you want to run.

## Official Raspberry Pi Camera Modules and Compatibility

Official Raspberry Pi camera modules are broadly compatible with Raspberry Pi computers that have CSI connectors. The main differences are not basic compatibility, but optical behavior, motion handling, lens flexibility, and how well each camera fits a particular scientific purpose.

In the table below, “Yes” means the camera can be used with that Raspberry Pi family. For Raspberry Pi 5, Raspberry Pi Zero 2 W, and most Compute Module IO boards, this usually requires the smaller 22-pin camera cable or an adapter.

| **Camera Module** | **Key Strengths** | **Pi 5** | **Pi 4** | **Zero 2 W** | **CM4** | **Best For** | **Less Suitable For** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Camera Module 3** | 12 MP, autofocus, compact, standard field of view, HDR support | Yes | Yes | Yes | Yes | General-purpose research recording, tabletop tasks, feeder cameras in daylight, classroom demonstrations | Very fast motion where rolling-shutter distortion matters, custom long-lens work |
| **Camera Module 3 Wide** | 12 MP, autofocus, wide field of view | Yes | Yes | Yes | Yes | Room coverage, cage or arena monitoring, group interaction scenes, wider context recording | Cases where subjects are small and distant and need tight framing |
| **Camera Module 3 NoIR / NoIR Wide** | Infrared-sensitive variants for use with IR illumination | Yes | Yes | Yes | Yes | Night observation, low-light feeder studies, dark enclosures with infrared lighting | Natural-color daylight recording where infrared sensitivity is not needed |
| **High Quality Camera** | 12.3 MP, interchangeable lenses, strong optical flexibility, external trigger support | Yes | Yes | Yes | Yes | Custom optics, telephoto views, controlled recording setups, experiments needing lens choice | Ultra-compact builds, very fast motion where global shutter is essential |
| **Global Shutter Camera** | Minimal motion distortion, short exposures, external trigger support, sync-friendly | Yes | Yes | Yes | Yes | Fast motion, biomechanics, human athletics, wing beats, synchronized machine vision | High-resolution wide-scene imaging where fine spatial detail is more important than shutter behavior |
| **AI Camera** | 12.3 MP intelligent vision sensor with on-sensor neural network acceleration | Yes | Yes | Yes | Yes | Low-latency object detection, edge AI prototypes, automated feeder alerts, embedded smart-camera workflows | Projects that need full flexibility in offline model design or traditional interchangeable optics |

This comparison highlights an important principle. “Compatible” does not mean “equally well matched.” A Camera Module 3 may connect perfectly to a Raspberry Pi Zero 2 W, but if the project demands real-time detection and local decision-making, a Raspberry Pi 5 may still be the more appropriate computer.

## Matching Hardware to Research Purpose

The most useful way to choose hardware is to begin with the biological or behavioral question. What are you trying to see? How fast does the subject move? How much light is available? Do you need local detection on the device, or can you record first and analyze later?

| **Research Scenario** | **Suggested Raspberry Pi** | **Suggested Camera** | **Why This Combination Works** | **Main Tradeoff** |
| --- | --- | --- | --- | --- |
| **Bird species detection at a feeder in daylight** | **Pi 5** if running local detection, **Pi 4** if mostly recording | **AI Camera** for local alerts, or **Camera Module 3** for record-first workflows | Good balance of resolution and field use; AI Camera is useful when the device should react on its own | AI workflow adds complexity; Camera Module 3 needs later analysis |
| **Bird feeder observation at night or dawn** | **Pi 4** or **Pi 5** | **Camera Module 3 NoIR** with IR illumination | Infrared sensitivity is more important here than natural daylight color | Requires infrared lighting and careful illumination design |
| **Tracking human athletes or fast limb motion** | **Pi 5** | **Global Shutter Camera** | Global shutter reduces distortion and supports short exposures for fast movement | Lower native resolution than the 12 MP modules |
| **Recording posture or interaction in a room or arena** | **Pi 4** or **Pi 5** | **Camera Module 3 Wide** | Wider field of view captures more of the space without custom optics | Subjects may appear smaller in the frame |
| **Longer-distance subject framing or custom optics** | **Pi 5** or **CM4** | **High Quality Camera** with a suitable lens | External lens choice gives much better control over magnification and framing | Larger, less plug-and-play, and more demanding to configure well |
| **Tiny embedded smart camera in a custom enclosure** | **CM4** or **Zero 2 W** | **Camera Module 3**, **NoIR**, or **AI Camera** depending task | Strong fit for purpose-built devices and low-profile installations | More engineering tradeoffs around thermals, power, and housing |

This scenario view is often more informative than any single specification. For example, a fast human athletics study may value shutter behavior more than megapixel count, whereas a feeder study may value low power, wireless convenience, or on-device alerts more than raw resolution.

## Low Light, Frame Rate, and Shutter Requirements

Raspberry Pi camera choices become much clearer when you ask three questions together:

  - How much light will be available?

  - How fast does the subject move?

  - Will the system record first or analyze on the device?

If the scene is dim and the subject moves slowly, a Camera Module 3 or HQ Camera may work well, especially if the experiment can tolerate moderate frame rates. If the subject moves quickly, then short shutter times become more important, and short shutter times need more light. In those cases, the Global Shutter Camera often becomes much more attractive, particularly when paired with strong illumination.

For night observation, a NoIR camera with infrared lighting is often more useful than simply increasing ISO and accepting noisy video. For local, always-on detection systems, the AI Camera or a Raspberry Pi 5 paired with another camera may be the better choice. Hardware choice is therefore always a balance between optics, motion, lighting, compute power, and analytic goals.

## Practical Compatibility Notes

Several practical issues matter before assembly begins:

  - **Connector size:** Raspberry Pi 4 uses the larger 15-pin CSI connector, while Raspberry Pi 5, Raspberry Pi Zero models, and most Compute Module IO boards use the smaller 22-pin connector.

  - **Cable choice:** Official cameras usually ship with a standard cable, but smaller boards often require a standard-to-mini cable or adapter.

  - **Cooling:** Raspberry Pi 5 is powerful, but real-time computer vision workloads may require active cooling.

  - **Storage:** Long video recordings quickly become large, so fast SD cards or external SSDs may matter.

  - **Lenses:** HQ and Global Shutter cameras are especially useful when your experiment requires a specific field of view or magnification.

  - **Lighting:** No camera choice can fully rescue poor lighting. Experimental illumination remains part of the measurement design.

## A Recommended Starter Build for LS100

For most LS100 students, the simplest and most flexible starting point is:

  - **Raspberry Pi 5** with **4 GB or 8 GB RAM**

  - **Camera Module 3** for standard framing, or **Camera Module 3 Wide** for room or arena coverage

  - **Official Raspberry Pi power supply**

  - **microSD card** of at least 64 GB

  - **Active cooling** if you plan to run sustained local processing on Raspberry Pi 5

This build is not the only good option, but it is the most forgiving. It supports modern software well, gives enough computing headroom for experimentation, and still keeps the system relatively simple. If your study requires night vision, replace the standard Camera Module 3 with a **NoIR** variant and add infrared illumination. If it requires very fast motion capture, replace it with the **Global Shutter Camera**.

## Hardware You Will Need

The table below lists the minimum parts needed to assemble a working Raspberry Pi computer vision camera, along with optional additions that become useful in research settings.

| **Component** | **Required?** | **Why It Matters** | **Recommended Starting Choice** |
| --- | --- | --- | --- |
| **Raspberry Pi computer** | Yes | The main computer that records and may analyze video | **Pi 5** for most students; **Pi 4** if mostly recording; **Zero 2 W** for very small deployments |
| **Camera module** | Yes | Determines field of view, motion handling, and low-light behavior | **Camera Module 3** or **Camera Module 3 Wide** |
| **CSI camera cable** | Yes | Physically connects the camera to the board | Standard 15-pin cable for **Pi 4**; standard-to-mini 22-pin cable for **Pi 5**, **Zero 2 W**, and many **CM4** setups |
| **microSD card** | Yes | Holds the operating system and often short recordings | 64 GB or larger, preferably a fast U3/V30 card |
| **Power supply** | Yes | Prevents instability during capture or processing | Official Raspberry Pi supply matched to the board |
| **Cooling** | Often | Helps prevent thermal throttling during sustained use | Active cooler or ventilated case for **Pi 5** |
| **Mount or tripod** | Strongly recommended | Stabilizes the camera and makes framing reproducible | Small tripod, clamp, or fixed bracket |
| **Keyboard, mouse, and monitor** | Optional | Useful for first setup if not working headless | Only needed for direct setup |
| **Network access** | Strongly recommended | Makes updating, remote login, and file transfer easier | Wi-Fi or Ethernet |
| **Infrared light** | Optional | Needed for dark recording with NoIR cameras | IR illuminator for night observation |
| **External SSD** | Optional | Useful for long or high-bitrate recordings | Especially useful on Pi 5 |

## Step 1: Choose Your Build Path

Before assembly, choose one of these simple starting paths:

  - **General-purpose daylight build:** Pi 5 + Camera Module 3 or Camera Module 3 Wide

  - **Night observation build:** Pi 5 or Pi 4 + Camera Module 3 NoIR + infrared light

  - **Fast-motion build:** Pi 5 + Global Shutter Camera + stronger illumination

The steps below are nearly identical across these options. The main differences are the camera module, cable type, and the lighting requirements.

## Step 2: Assemble the Hardware

1. Power the Raspberry Pi fully off before connecting the camera.

2. Insert the microSD card if you have already prepared it, or set it aside for later if you will flash the operating system first.

3. Open the CSI camera connector latch gently.

4. Insert the ribbon cable evenly and fully. On the Raspberry Pi side, the metal contacts face away from the connector flap. On the camera side, the cable should be seated firmly according to the board markings, with the contacts aligned correctly.

5. Close the connector latch carefully so the ribbon cable is held in place.

6. Mount the camera in a stable orientation. For a feeder or small enclosure, a fixed bracket is often best. For testing indoors, a tabletop tripod is usually enough.

7. If you are using a Pi 5 and expect sustained processing, install the active cooler or use a ventilated case.

8. Connect power only after the cable is seated and the camera is mounted securely.

The most common early build failure is a mis-seated ribbon cable, especially when switching between 15-pin and 22-pin connectors. If the camera is not detected later, the cable should be the first thing you re-check.

## Step 3: Install Raspberry Pi OS

The simplest setup path is to use **Raspberry Pi Imager** on your laptop or desktop computer.

1. Open Raspberry Pi Imager.

2. Choose your Raspberry Pi board.

3. Choose **Raspberry Pi OS (64-bit)** for Pi 4, Pi 5, or CM4. For Zero 2 W, Raspberry Pi OS Lite is often a good choice if you want a lightweight remote setup.

4. Select your microSD card.

5. Use the advanced settings menu to pre-configure:

   - hostname
   - username and password
   - Wi-Fi credentials
   - SSH access
   - locale and keyboard settings

6. Flash the card, eject it safely, and insert it into the Raspberry Pi.

For research deployments, enabling SSH during imaging is extremely useful because it allows the Raspberry Pi to be managed remotely without a dedicated screen or keyboard.

## Step 4: First Boot and Basic Setup

Boot the Raspberry Pi and allow the initial setup to complete. Then update the system:

```bash
sudo apt update
sudo apt full-upgrade -y
sudo reboot
```

After rebooting, confirm that the system is healthy and reachable over the network if you plan to run it headless.

Current Raspberry Pi OS versions usually auto-detect official camera modules, so in most cases you do not need to manually enable a legacy camera interface. Using an up-to-date operating system is more important than older camera-enabling workflows.

## Step 5: Verify That the Camera Is Detected

Once the system is updated, test whether Raspberry Pi can see the camera:

```bash
rpicam-hello --list-cameras
```

If the camera is detected correctly, you can launch a live preview:

```bash
rpicam-hello -t 0
```

For a headless setup without a display, capture a still image directly instead:

```bash
rpicam-still -n -o first_test.jpg
```

If this step fails, do not move forward yet. Re-check the ribbon cable, connector type, power stability, and whether the camera module matches the board-side cable.

## Step 6: Capture Your First Still Image and Video Clip

Once the camera is recognized, create a first test still image:

```bash
rpicam-still -o first_still.jpg
```

Then capture a short video clip:

```bash
rpicam-vid -t 5000 -o first_clip.h264
```

These two files are your first quality-control checkpoint. Review them carefully for:

  - framing

  - focus

  - lighting

  - motion blur

  - background clutter

For behavioral research, the first successful capture is not just a proof that the camera works. It is the first chance to judge whether the visual information needed by the study is actually present.

## Step 7: Test the Camera from Python

If you want students to move quickly from hardware setup into Python workflows, a minimal **Picamera2** test is useful. Install the library if needed:

```bash
sudo apt install -y python3-picamera2
```

Then create a short test script such as:

```python
from picamera2 import Picamera2
from time import sleep

camera = Picamera2()
camera.configure(camera.create_still_configuration())
camera.start()
sleep(2)
camera.capture_file("python_test.jpg")
camera.stop()
```

Run it with:

```bash
python3 camera_test.py
```

This step matters because it confirms that the camera is not only physically connected, but also available from a Python workflow, which is how many LS100 students will later interact with it.

## Step 8: Build a Recording Setup That Supports Measurement

A camera build becomes a research tool only when the recording setup is stable enough to support repeated observation. Before collecting real data, establish a repeatable capture arrangement.

Use this checklist:

  - Fix the camera position so it does not shift between sessions.

  - Keep lighting as stable as possible across recordings.

  - Decide whether autofocus is helpful or whether a stable fixed focus is better.

  - Include enough contrast between the subject and the background.

  - Avoid unnecessary background motion such as leaves, screens, or moving shadows if they may interfere with analysis.

  - Record a pilot clip and inspect it at the frame level before starting the full experiment.

For many behavioral studies, a visually beautiful image is less important than a stable, analyzable one.

## Step 9: Starter Recording Profiles by Use Case

The table below gives practical starting points rather than strict prescriptions. These are intended as first test configurations that students can refine after reviewing pilot recordings.

| **Use Case** | **Suggested Hardware** | **Starting Recording Goal** | **What to Check First** |
| --- | --- | --- | --- |
| **Daylight bird feeder recording** | Pi 4 or Pi 5 + Camera Module 3 | Clear subject framing, stable daylight exposure, moderate frame rate | Can the bird fill enough of the frame for later detection or classification? |
| **Night feeder observation** | Pi 4 or Pi 5 + Camera Module 3 NoIR + IR light | Reliable visibility without visible-light disturbance | Is the IR illumination even, and does the subject remain identifiable? |
| **Room or arena interaction recording** | Pi 4 or Pi 5 + Camera Module 3 Wide | Wide coverage with enough detail for posture or movement interpretation | Are subjects large enough in the frame for later tracking? |
| **Human athletics or fast limb motion** | Pi 5 + Global Shutter Camera | Short exposure and reduced motion distortion | Is there enough light to support fast capture without blur? |
| **Long-distance framing or lens-controlled setup** | Pi 5 or CM4 + HQ Camera | Optical control over magnification and scene coverage | Does the chosen lens provide enough detail without making the scene too narrow? |

## Step 10: Troubleshooting Common Problems

| **Problem** | **Likely Cause** | **What to Try** |
| --- | --- | --- |
| **Camera not detected** | Ribbon cable misaligned, wrong cable type, connector not fully seated | Re-seat the cable carefully, confirm 15-pin versus 22-pin cable type, update Raspberry Pi OS |
| **Image is very dark or noisy** | Not enough light, unsuitable exposure settings, wrong camera for the lighting conditions | Add light, reduce frame rate if possible, use NoIR plus IR illumination for dark settings |
| **Fast motion looks smeared or bent** | Rolling shutter distortion or shutter too slow | Use stronger light, shorten exposure, or move to the Global Shutter Camera |
| **Pi 5 becomes hot or slows down** | Thermal throttling during sustained processing | Add active cooling, improve airflow, reduce on-device workload |
| **Files become too large** | Resolution, frame rate, or recording duration too high | Use shorter pilot clips, lower frame rate where acceptable, move long recordings to external storage |
| **Tracking later fails** | Subject too small, low contrast, cluttered background, unstable camera position | Reframe the scene, improve lighting, simplify the background, stabilize the mount |

## From Prototype to Research Device

At this stage, students should have a working Raspberry Pi camera, a first still image, a first video clip, and a basic Python test. That is enough to begin asking the next scientific question: is this recording setup good enough for the behavior I want to study?

The best next step is not to collect a large dataset immediately. It is to run short pilot recordings, review them frame by frame, and decide whether the current build preserves the relevant visual information. If it does, the system can move into experimental use. If it does not, the needed changes are usually clear: more light, a wider view, a longer lens, a different camera module, or a higher-powered Raspberry Pi.