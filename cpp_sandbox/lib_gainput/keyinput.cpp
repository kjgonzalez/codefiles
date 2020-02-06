/*
date: 200119
objective: get a minimal example of gainput, as simplified as possible. only
    keyboard input

*/
#include <iostream>
#include <gainput/gainput.h>
#include <X11/Xlib.h>
#include <X11/Xatom.h>
#include <GL/glx.h>

using namespace std;
// Define your user buttons
enum Button{
    bUp,
    bLeft,
    bDown,
    bRight,
    bQuit
};

const char* windowName = "Control Input ('q' to quit)";
const int width = 20;const int height = 1;

int main(int argc, char** argv){
    static int attributeListDbl[] = {GLX_RGBA,GLX_DOUBLEBUFFER,
        GLX_RED_SIZE, 1, GLX_GREEN_SIZE, 1, GLX_BLUE_SIZE, 1, None};

    Display* xDisplay = XOpenDisplay(0);
    if (xDisplay == 0){
        cerr << "Cannot connect to X server." << endl;
        return -1;
    }//if

    Window root = DefaultRootWindow(xDisplay);
    XVisualInfo* vi = glXChooseVisual(xDisplay, DefaultScreen(xDisplay), attributeListDbl);
    assert(vi);

    GLXContext context = glXCreateContext(xDisplay, vi, 0, GL_TRUE);
    Colormap cmap = XCreateColormap(xDisplay, root, vi->visual, AllocNone);

    XSetWindowAttributes swa;
    swa.colormap = cmap;
    swa.event_mask = ExposureMask | KeyPressMask | KeyReleaseMask
        | PointerMotionMask | ButtonPressMask | ButtonReleaseMask;

    Window xWindow = XCreateWindow(
            xDisplay, root, 0, 0, width, height, 0,
            CopyFromParent, InputOutput, CopyFromParent, CWEventMask, &swa);

    glXMakeCurrent(xDisplay, xWindow, context);
    XSetWindowAttributes xattr;
    xattr.override_redirect = False;
    XChangeWindowAttributes(xDisplay, xWindow, CWOverrideRedirect, &xattr);

    XMapWindow(xDisplay, xWindow);
    XStoreName(xDisplay, xWindow, windowName);

    // Setup Gainput
    gainput::InputManager manager;
    const gainput::DeviceId keyboardId = manager.CreateDevice<gainput::InputDeviceKeyboard>();

    gainput::InputMap map(manager);
    map.MapBool(bUp, keyboardId, gainput::KeyW); // case insensitive
    map.MapBool(bLeft, keyboardId, gainput::KeyA);
    map.MapBool(bDown, keyboardId, gainput::KeyS);
    map.MapBool(bRight, keyboardId, gainput::KeyD);
    map.MapBool(bQuit, keyboardId, gainput::KeyQ);

    // manager.SetDisplaySize(width, height);

    for (;;){
        // Update Gainput
        manager.Update();

        XEvent event;
        while (XPending(xDisplay)){
            XNextEvent(xDisplay, &event);
            manager.HandleEvent(event);
        }//while

        // Check button states
        if(map.GetBoolWasDown(bUp)){cout << "Up" << endl;}
        if(map.GetBoolWasDown(bLeft)){cout << "Left" << endl;}
        if(map.GetBoolWasDown(bDown)){cout << "Down" << endl;}
        if(map.GetBoolWasDown(bRight)){cout << "Right" << endl;}
        if(map.GetBoolWasDown(bQuit)){cout << "Exiting..." << endl;break;}

    }//for

    // XDestroyWindow(xDisplay, xWindow);
    // XCloseDisplay(xDisplay);

    return 0;
}//main
