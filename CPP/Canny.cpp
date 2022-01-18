#include<iostream>
#include"opencv2/highgui.hpp"
#include"opencv2/imgproc.hpp"
#include<string>
#include<cmath>

using namespace std;
using namespace cv;

int main(void) {
    string name = "./edge.jpg";
    Mat input = imread(name, CV_LOAD_IMAGE_GRAYSCALE);

    GaussianBlur(input, input, Size(5, 5), 1.5);
    Mat first;
    Mat second;
    Sobel(input, first, -1, 1, 0);
    Sobel(input, second, -1, 0, 1);


    Mat preoutput = Mat::zeros(Size(input.rows, input.cols), CV_16UC1);
    for (int i = 0; i < input.rows; ++i) {
        for (int j = 0; j < input.cols; ++j) {
            char centerX = second.at<uchar>(i, j);
            char centerY = first.at<uchar>(i, j);
            double center = sqrt(centerY * centerY + centerX * centerX);
            preoutput.at<ushort>(i, j) = (ushort) center;
        }
    }

    Mat aaa = input.clone();
    for (int i = 0; i < input.rows; ++i) { 
        for (int j = 0; j < input.cols; ++j) {
            aaa.at<uchar>(i, j) = saturate_cast<uchar>(preoutput.at<ushort>(i, j));
        }
    }


    for (int i = 1; i < input.rows - 1; i++) { 
        for (int j = 1; j < input.cols - 1; j++) {
            float degree = atan((float) (first.at<uchar>(i, j)) / second.at<uchar>(i, j)) / CV_PI * 180;
            int center = preoutput.at<ushort>(i, j);
            if (degree > -22.5 && degree <= 22.5) { // 0 degree
                int left = preoutput.at<ushort>(i - 1, j);
                int right = preoutput.at<ushort>(i + 1, j);
                if (center <= left || center <= right) {
                    preoutput.at<ushort>(i, j) = 0;
                }

            }
            else if (degree > -67.5 && degree <= -67.5) { // 90 degree
                int left = preoutput.at<ushort>(i, j - 1);
                int right = preoutput.at<ushort>(i, j + 1);
                if (center <= left || center <= right) {
                    preoutput.at<ushort>(i, j) = 0;
                }
            }
            else if (degree > 22.5 && degree <= 67.5) { // 45 degree
                int left = preoutput.at<ushort>(i + 1, j - 1);
                int right = preoutput.at<ushort>(i - 1, j + 1);
                if (center <= left || center <= right) {
                    preoutput.at<ushort>(i, j) = 0;
                }
            }
            else if (degree > -67.5 && degree <= -22.5) { // 135 degree
                int left = preoutput.at<ushort>(i - 1, j - 1);
                int right = preoutput.at<ushort>(i + 1, j + 1);
                if (center <= left || center <= right) {
                    preoutput.at<ushort>(i, j) = 0;
                }
            }else{
                preoutput.at<ushort>(i, j) = 0;
            }
        }
    }

    Mat bbb = input.clone();
    for (int i = 0; i < input.rows; ++i) { 
        for (int j = 0; j < input.cols; ++j) {
            bbb.at<uchar>(i, j) = saturate_cast<uchar>(preoutput.at<ushort>(i, j));
        }
    }

    Mat final = Mat::zeros(Size(input.rows, input.cols), CV_8UC1);
    for (int i = 0; i < input.rows; i++) {
        for (int j = 0; j < input.cols; j++) {
            final.at<uchar>(i, j) = saturate_cast<uchar>(preoutput.at<ushort>(i, j));
        }
    }


    int lower = 30, upper = 70;


    Mat realfinal = Mat::zeros(Size(input.rows, input.cols), CV_8UC1);
    for (int i = 1; i < input.rows - 1; i++) {
        for (int j = 1; j < input.cols - 1; j++) {
            if (final.at<uchar>(i, j) >= upper) {
                realfinal.at<uchar>(i, j) = 255;
            } else if (final.at<uchar>(i, j) > lower) {
                int count = 0;
                if (final.at<uchar>(i - 1, j) >= upper) count++;
                if (final.at<uchar>(i + 1, j) >= upper) count++;
                if (final.at<uchar>(i - 1, j + 1) >= upper) count++;
                if (final.at<uchar>(i - 1, j - 1) >= upper) count++;
                if (final.at<uchar>(i + 1, j + 1) >= upper) count++;
                if (final.at<uchar>(i + 1, j - 1) >= upper) count++;
                if (final.at<uchar>(i, j - 1) >= upper) count++;
                if (final.at<uchar>(i, j + 1) >= upper) count++;
                if (count >= 2) realfinal.at<uchar>(i, j) = 255;
            }
        }
    }

    imshow("realfinal", realfinal);

    waitKey(0);
    return 0;
}
