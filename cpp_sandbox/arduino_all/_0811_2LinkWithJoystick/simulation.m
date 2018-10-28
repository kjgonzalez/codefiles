% program: 2 link simulation. assume all movement in vertical-horizontal
% axes, such as x-y plane

% steps:
% 1. start simulation at 1,1
% 2. move in small increments to 3,1
% 3. move to 3,3
% 4. move to 1,3
% 5. finish back at 1,1
% 
% simulation complete
% 
% configuration: "elbow down" / right arm

%update: works!!! (0811'14)

%constants
r1=2.5;
r2=2.5;

% initial locations
xd=1;
yd=1;

for i=1:.1:3
    xd=i;

    %calculate everything here
    % get angles from desired location
    R = sqrt(xd^2+yd^2);
    phi = acos(xd/R);
    beta=acos((r1^2+R^2-r2^2)/(2*R*r1));
    gamma=acos((r2^2+R^2-r1^2)/(2*R*r2));
    a1=phi+beta; %CHANGE HERE FOR ELBOW CONFIG
    a2=beta+gamma;
    %calculate where everything should be: 
    x1=r1*cos(a1);
    y1=r1*sin(a1);
    x2=x1+r2*cos(a1-a2); %CHANGE HERE FOR ELBOW CONFIG
    y2=y1+r2*sin(a1-a2); %CHANGE HERE FOR ELBOW CONFIG

    
    %plot everything
    clf;
    hold on;
    plotline([-2 -2],[4 4],'k.');
    plot(xd,yd,'ro');
    plot(0,0,'ko');
    plotline([0 0], [x1 y1],'b-');
    plot([x1 x2],[y1 y2],'bx');
    plotline([x1 y1],[x2 y2],'b-');
    pause(.005)
end %forloop (1,1 to 3,1)
% 
% for i = 1:.1:3
%     yd=i;
%     % get angles from desired location
%     R = sqrt(xd^2+yd^2);
%     phi = acos(xd/R);
%     beta=acos((r1^2+R^2-r2^2)/(2*R*r1));
%     gamma=acos((r2^2+R^2-r1^2)/(2*R*r2));
%     a1=phi-beta;
%     a2=beta+gamma;
%     %calculate where everything should be: 
%     x1=r1*cos(a1);
%     y1=r1*sin(a1);
%     x2=x1+r2*cos(a1+a2);
%     y2=y1+r2*sin(a1+a2);
%     %plot everything
%     clf;
%     hold on;
%     plotline([-2 -2],[4 4],'k.');
%     plot(xd,yd,'ro');
%     plot(0,0,'ko');
%     plotline([0 0], [x1 y1],'b-');
%     plot([x1 x2],[y1 y2],'bx');
%     plotline([x1 y1],[x2 y2],'b-');
%     pause(.005)
% 
% end
% 
% for i=3:-.1:1
% 
%     xd=i;
%     % get angles from desired location
%     R = sqrt(xd^2+yd^2);
%     phi = acos(xd/R);
%     beta=acos((r1^2+R^2-r2^2)/(2*R*r1));
%     gamma=acos((r2^2+R^2-r1^2)/(2*R*r2));
%     a1=phi-beta;
%     a2=beta+gamma;
%     %calculate where everything should be: 
%     x1=r1*cos(a1);
%     y1=r1*sin(a1);
%     x2=x1+r2*cos(a1+a2);
%     y2=y1+r2*sin(a1+a2);
%     %plot everything
%     clf;
%     hold on;
%     plotline([-2 -2],[4 4],'k.');
%     plot(xd,yd,'ro');
%     plot(0,0,'ko');
%     plotline([0 0], [x1 y1],'b-');
%     plot([x1 x2],[y1 y2],'bx');
%     plotline([x1 y1],[x2 y2],'b-');
%     pause(.005)
% end
% 
% for i=3:-.1:1
% 
%     yd=i;
%     % get angles from desired location
%     R = sqrt(xd^2+yd^2);
%     phi = acos(xd/R);
%     beta=acos((r1^2+R^2-r2^2)/(2*R*r1));
%     gamma=acos((r2^2+R^2-r1^2)/(2*R*r2));
%     a1=phi-beta;
%     a2=beta+gamma;
%     %calculate where everything should be: 
%     x1=r1*cos(a1);
%     y1=r1*sin(a1);
%     x2=x1+r2*cos(a1+a2);
%     y2=y1+r2*sin(a1+a2);
%     %plot everything
%     clf;
%     hold on;
%     plotline([-2 -2],[4 4],'k.');
%     plot(xd,yd,'ro');
%     plot(0,0,'ko');
%     plotline([0 0], [x1 y1],'b-');
%     plot([x1 x2],[y1 y2],'bx');
%     plotline([x1 y1],[x2 y2],'b-');
%     pause(.005)
% end
% 
