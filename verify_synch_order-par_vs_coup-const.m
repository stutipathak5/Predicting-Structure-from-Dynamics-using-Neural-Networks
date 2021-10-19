global N omega a

% select which to verify erdos-reyni("er") or scale free("sf") graph
graph_type= "er"

if graph_type== "er"
a=load('ER+SF_New/er60.txt');
else
a=load('ER+SF_New/sf60.txt');
end

N=size(a,1)
omega=generate_random(0.5,N);
y0=(generate_random(pi,N))';
tspan=0:0.01:400;
rr2=[];
m=10000;

lamda=0
lam=[]
for k=1:60
    del_lamda=0.0025;
    lamda=(k-1)*del_lamda
    [t,y]=ode45(@(t,y)odefm(t,y,lamda),tspan,y0);
    size(y)
    y=wrapToPi(y);
    sz1=size(y,1);
    r= order_par(y((sz1-m):sz1,:))
    rr2=[rr2,r];
    lam=[lam;lamda]
    disp(k);
end
set(0, 'DefaultAxesFontSize', 14)
plot(lam,rr2,'-o')
xlabel('{\lambda}')
ylabel('r')
if graph_type== "er"
title('ER random (N=100, <k>=18)')
else
title('scale free (N=100, <k>=18)')
end


function theta_dot = odefm(~,theta,lamda)
     global omega a
     theta_dot = omega + lamda*sum(a.*sin(theta-theta'))';
end


function rr=generate_random(range,no_points)
rr=range*rand(no_points,1);
for i=1:no_points
   if(rand(1,1)<0.5)
   rr(i)=-rr(i);
   end
end
end

function r=order_par(x)
global N
r1=abs((sum(exp(1i*x),2))/N);
R=mean(r1);
r=R;
end
