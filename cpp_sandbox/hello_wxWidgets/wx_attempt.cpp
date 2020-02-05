/*
date: 200205
objective: first time compile of wxWidgets to ensure wxwidgets works

How to Compile: 
    (assume code and CMakeLists files created)
    cmake .
    make 
    (run file)

NOTES: 
* KJG020205: This works on linux side
* be sure to include proper items in CMakeLists


*/

#include <wx/wx.h>

class Simple : public wxFrame
{
public:
    Simple(const wxString& title)
		: wxFrame(NULL, wxID_ANY, title, wxDefaultPosition, wxSize(250, 150))
	{
		Centre();
	}
};

class MyApp : public wxApp
{
public:
	bool OnInit()
	{
		Simple *simple = new Simple(wxT("Window Title"));
		simple->Show(true);
		return true;
	}
};

wxIMPLEMENT_APP(MyApp);
