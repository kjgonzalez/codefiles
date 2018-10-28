% main objective of code: 
% simulate robot detecting a wall 
% at a random angle, then have it 
% decide what angle it's at

% ALL DIST UNITS IN CM
clf;
hold on;

% boundaries, square area
bound=30;

plot([-bound bound],[-bound bound],'k.');
plotcircle(5,[0 0]);
plotline([0 0],[0 bound],'k:');

% want to generate 'random' points
... for the robot to detect

% will generate some angle generally between 20 and 60
angle=(rand(1)+rand(1))/2*80;
m=tand(angle); %slope
b=bound-10; %intercept

x=[0 -1 -2 -3]*10;
y=m*(x+rand(size(x))*5)+b;
plot(x,y,'rx')

yideal=m*(x)+b;
plot(x,yideal,'b:');

% get (r,th) values, convert to (x,y) values, do linear regression

m1=0;

xavg=mean(x);
yavg=mean(y);
a=0;
b=0;
for i=1:length(x)
    a=a+(x(i)-xavg)*(y(i)-yavg);
    b=b+(x(i)-xavg)^2;
end %forloop
m1=a/b;

m1/m*100
y1=m1*x+y(1);
plot(x,y1,'g-');


