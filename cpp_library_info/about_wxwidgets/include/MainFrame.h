#pragma once
#include <wx/wx.h>

#define LESSON 6 // 3=basics, 5=static_events, 6=dynamic_events (better)

class MainFrame : public wxFrame
{
public:
    MainFrame(const wxString& title);
private:
    void OnButtonClicked(wxCommandEvent& evt); // for lesson5: events (static handling?)
    void OnSliderChanged(wxCommandEvent& evt);
    void OnTextChanged(wxCommandEvent& evt);
    
#if(LESSON==5)
    wxDECLARE_EVENT_TABLE();
#endif
};


// eof
