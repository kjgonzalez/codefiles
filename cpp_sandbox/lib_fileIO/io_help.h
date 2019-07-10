/*
Date created: 190710
Author: kris gonzalez
Objective: Create simplified, easy-to-use file i/o class that can be used where
    needed.
*/

class FileOpen{
    std::ifstream fin;
    std::ofstream fout;
    char mode;
    std::string filename;
public:
    FileOpen(std::string _filename,char _mode='r'){
        filename=_filename;
        mode = _mode;
        if(mode=='w'){
            fout.open(filename.c_str());
        }//if-'w'

        else if(mode=='r'){
            // printf("read mode\n");
            fin.open(filename.c_str());
        }//if-'r'
        else printf("WARNING: MODE NOT RECOGNIZED.\n");
    }//initialize

    // getters / setters
    char get_mode(){return mode;}
    std::string get_filename(){return filename;}

    // write functions
    bool write(std::string text){
        /* write out a line of text to file */
        if(mode!='w'){
            printf("WARNING: INCORRECT MODE.\n");
            return false;
        } //mode-check
        fout << text.c_str();
        return true;
    }//write

    //read functions
    std::string readline(){
        /* read out one line of text */
        std::string line;
        if(mode!='r'){
            printf("WARNING: INCORRECT MODE.\n");
            return line;
        }//mode-check
        getline(fin,line);
        line+="\n";
        return line;
    }//readline

    std::vector<std::string> readall(){
        /* return entire file in string vector */
        std::vector<std::string> raw;
        if(mode!='r'){
            printf("WARNING: INCORRECT MODE.\n");
            return raw;
        }//if-wrong-mode
        fin.seekg(0,fin.beg); // go to start of filestream
        std::string line;
        while(!fin.eof()){
            getline(fin,line);
            line+="\n";
            raw.push_back(line);
            }
        return raw;
    }//readall

    // general functions
    bool close(){
        /* close the current stream */
        if(mode=='w') fout.close();
        else if(mode=='r') fin.close();
        else{printf("WARNING: INCORRECT MODE.\n"); return false;}
        return true;
    }//close

}; //class FileOpen
