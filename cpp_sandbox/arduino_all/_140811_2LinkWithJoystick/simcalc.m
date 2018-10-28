function [temp] = simcalc(xd,yd)

    r1=15.5;
    r2=16;

    R = sqrt(xd^2+yd^2);
    phi = acos(xd/R);
    beta=acos((r1^2+R^2-r2^2)/(2*R*r1));
    gamma=acos((r2^2+R^2-r1^2)/(2*R*r2));
    a1=phi+beta; %CHANGE HERE FOR ELBOW CONFIG
    a2=beta+gamma;
    a1=a1*180/pi;
    a2=a2*180/pi;
    
    temp = [a1, a2];
end