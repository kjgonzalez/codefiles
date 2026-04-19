#include <wx/wx.h>
#include "App.h"
#include "MainFrame.h"

wxIMPLEMENT_APP(App); // starts application here

bool App::OnInit()
{
    MainFrame* mainFrame = new MainFrame("C++ GUI");
    mainFrame->SetClientSize(800, 600);
    mainFrame->Center();
    mainFrame->Show();
    return true; // processing should continue, otherwise quit
}




//eof
