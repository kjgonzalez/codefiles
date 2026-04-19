/*
implementation of GUI layout

root object expands to fill window, so first item needs to fill whole space

todos:
* password field
* scrollbar?
* GUI designer, e.g. https://wiki.wxwidgets.org/Tools
* kb/m events

*/
#include "MainFrame.h"
#include "wx/spinctrl.h"



#if(LESSON==5)
enum IDs {
    BUTTON_ID = 2,
    SLIDER_ID = 3,
    TEXT_ID = 4
};

// bind events in static method. note these are macros, no ';' needed.
wxBEGIN_EVENT_TABLE(MainFrame, wxFrame)
EVT_BUTTON(BUTTON_ID, MainFrame::OnButtonClicked)
EVT_SLIDER(SLIDER_ID, MainFrame::OnSliderChanged)
EVT_TEXT(TEXT_ID, MainFrame::OnTextChanged)
wxEND_EVENT_TABLE()
#endif


MainFrame::MainFrame(const wxString& title) : wxFrame(nullptr, wxID_ANY, title)
{
    wxPanel* panel = new wxPanel(this);
#if(LESSON==3)
    wxButton* button = new wxButton(panel, wxID_ANY, "Button", wxPoint(150, 50), wxSize(100, 35));
    auto checkBox = new wxCheckBox(panel, wxID_ANY, "CheckBox", wxPoint(550, 55));
    auto staticText = new wxStaticText(panel, wxID_ANY, "staticText", wxPoint(120, 150));
    auto textCtrl = new wxTextCtrl(panel, wxID_ANY, "text editable", wxPoint(500, 145), wxSize(200, -1));
    auto slider = new wxSlider(panel, wxID_ANY, 25, 0, 100, wxPoint(100, 250), wxSize(200, -1));
    auto  gauge = new wxGauge(panel, wxID_ANY, 100, wxPoint(500, 255), wxSize(200,-1));
    gauge->SetValue(50);

    // combobox
    wxArrayString choices;
    choices.Add("item a");
    choices.Add("item b");
    choices.Add("item c");
    auto choice = new wxChoice(panel, wxID_ANY, wxPoint(150, 375), wxSize(100, -1), choices);
    choice->Select(1);

    // numerical spin control
    auto spinCtrl = new wxSpinCtrl(panel, wxID_ANY, "", wxPoint(550, 375), wxSize(100, -1));

    auto listbox = new wxListBox(panel, wxID_ANY, wxPoint(150, 475), wxSize(100, -1), choices);

    auto radiobox = new wxRadioBox(panel, wxID_ANY, "RadioBox", wxPoint(485, 475), wxDefaultSize, choices);

    // tip: don't allocate new controls on the stack can cause problems...
    //   wxwidgets takes care of memory control
    
#elif(LESSON==5)
    auto button = new wxButton(panel, BUTTON_ID, "Button", wxPoint(300, 275), wxSize(200, 50));
    auto slider = new wxSlider(panel, SLIDER_ID, 0, 0, 100, wxPoint(300, 200), wxSize(200, -1));
    auto text = new wxTextCtrl(panel, TEXT_ID, "", wxPoint(300, 375), wxSize(200, -1));
#elif(LESSON==6)
    auto button = new wxButton(panel, wxID_ANY, "Button", wxPoint(300, 275), wxSize(200, 50));
    auto slider = new wxSlider(panel, wxID_ANY, 0, 0, 100, wxPoint(300, 200), wxSize(200, -1));
    auto text = new wxTextCtrl(panel, wxID_ANY, "", wxPoint(300, 375), wxSize(200, -1));
    
    // add bind events
    button->Bind(wxEVT_BUTTON, &MainFrame::OnButtonClicked, this); // not bad, that's everything
    slider->Bind(wxEVT_SLIDER, &MainFrame::OnSliderChanged, this); // event types are listed in documentation
    text->Bind(wxEVT_TEXT, &MainFrame::OnTextChanged, this);

    // to unbind, need separate function
    button->Unbind(wxEVT_BUTTON, &MainFrame::OnButtonClicked, this);

#else
    auto staticText = new wxStaticText(panel, wxID_ANY, "INVALID LESSON NUMBER SELECTED", wxPoint(10,10));

#endif
    CreateStatusBar();


}

void MainFrame::OnButtonClicked(wxCommandEvent& evt) { wxLogStatus("Button Clicked"); }
void MainFrame::OnSliderChanged(wxCommandEvent& evt)
{
    wxString str = wxString::Format("Slider Value: %d", evt.GetInt());
    wxLogStatus(str);
}
void MainFrame::OnTextChanged(wxCommandEvent& evt)
{
    wxString str = wxString::Format("Text: %s", evt.GetString());
    wxLogStatus(str);

}



//eof
