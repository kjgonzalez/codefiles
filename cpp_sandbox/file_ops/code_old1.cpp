/*
Author: Kris Gonzalez
DateCreated: 180528
Objective: demo basic usage of file in / out operations

things to display:
how to write out to a file (preferrably csv)
how to read from a file.
*/

#include <iostream>	//general screen i/o operations
#include <time.h>	// want to ensure printing out new info
#include <fstream>	//enables in/out file manipulation

//trying to create array of strings
#include <bits/stdc++.h>

std::vector<std::string> getConfig(char * filename){
	/* Objective: load config file from a text file, return string values.
	ASSUMPTIONS:
		* skip first line
		* only save values after the comma
		* ORDER IS NOT CHANGED
	*/
	std::ifstream f;
	std::string iline;
	std::vector<std::string> configvals;
	f.open(filename);
	std::getline(f,iline); // ignore first line
	while(!f.eof()){
		std::getline(f,iline);
		iline = iline.substr(iline.find(",")+1); //line is now a substring
		configvals.push_back(iline); //add to vector
		std::cout << "substring: "<< iline << "\n"; //show on screen


	}//while not at eof
}//getConfig





int main(){
	// step 1: write out to a file
	std::ofstream myfile;
	myfile.open("fileout.txt");
	std::cout << "file opened...\n";
	for(int i =0;i<3;i++)
		myfile << "this line written at ..." << time(NULL) << "\n";
	myfile.close();
	std::cout << "file closed...\n";

	// step 2: read in from a file
	std::string line;
	std::ifstream f;
	f.open("readme.csv");
	if(f.is_open()){
		// able to perform operations
		std::cout << "reading out file contents...\n";
		while(!f.eof()){
			std::getline(f,line); //put data of a line into string var
			std::cout << line << "\n";
		}//while not at eof
		// once at file eof, close.
		f.close();
	}//if file successfully opened
	else std::cout << "Unable to open file\n";


	//temp: want to create array of strings, using vectors
	std::vector<std::string> color;
	color.push_back("Blue");
	color.push_back("Red");
	color.push_back("Orange");
	color.push_back("Yellow");
// 	for (int i=0;i<color.size();i++){ //now display results
// 		std::cout << color[i] << "\n";
// 	}//for-display colors

	//temp: return a substring based on a search value (,)
	std::cout << "figuring out a substring... \n";
	std::cout << line << "\n";
	std::cout << line.length() << "\n";
	std::cout << "location of comma: " << line.find(",") << "\n";
	// return substring of desired value:
	std::cout << "substring: "<< line.substr(line.find(",")+1) << "\n";
	//temp: want to return subset of string array based on split by ','

	//will use "line" value, since it already has neecssary string of "pub_topic,sample3"
	getConfig("readme.csv");


	return 0;
}//int main
