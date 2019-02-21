<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1550056860755" ID="ID_1003418571" MODIFIED="1550056881870" STYLE="fork" TEXT="KJG Thesis">
<node CREATED="1550056889927" ID="ID_208024305" MODIFIED="1550056939743" POSITION="right" TEXT="General Steps"/>
<node CREATED="1550056894669" ID="ID_709956119" MODIFIED="1550056903165" POSITION="left" TEXT="Admin">
<node CREATED="1550056954895" ID="ID_1871385759" MODIFIED="1550763487181" TEXT="Start Date">
<node COLOR="#ff0000" CREATED="1550763508633" ID="ID_1959295405" MODIFIED="1550763515083" TEXT="190401"/>
</node>
<node CREATED="1550763487647" ID="ID_1188110960" MODIFIED="1550763489262" TEXT="Due Date">
<node COLOR="#ff0000" CREATED="1550763490370" ID="ID_371618095" MODIFIED="1550763515074" TEXT="190930"/>
</node>
<node COLOR="#ff0000" CREATED="1550056959661" ID="ID_1656773456" MODIFIED="1550763606057" TEXT="Is paperwork turned in?">
<node COLOR="#ff0000" CREATED="1550763518336" ID="ID_563345429" MODIFIED="1550763588664" TEXT="no, due 190320"/>
<node CREATED="1550763532928" ID="ID_1315302174" MODIFIED="1550763537253" TEXT="required items">
<node COLOR="#ff0000" CREATED="1550763537983" ID="ID_1166427713" MODIFIED="1550763603024" TEXT="proposal">
<node COLOR="#ff0000" CREATED="1550763547119" ID="ID_1294366791" MODIFIED="1550763590463" TEXT="due 190315"/>
</node>
<node CREATED="1550763577641" ID="ID_35225567" MODIFIED="1550763583661" TEXT="verbal agreement from Elser"/>
<node CREATED="1550763563011" ID="ID_726810338" MODIFIED="1550763569260" TEXT="signature from Ertel"/>
<node CREATED="1550763558141" ID="ID_670442254" MODIFIED="1550763562666" TEXT="signature from Ruf"/>
<node CREATED="1550763569738" ID="ID_593883082" MODIFIED="1550763574090" TEXT="Signature from administration"/>
</node>
</node>
<node CREATED="1550763625010" ID="ID_505537359" MODIFIED="1550763629515" TEXT="is this project specific enough?">
<node COLOR="#ff0000" CREATED="1550763629991" ID="ID_799042208" MODIFIED="1550763644335" TEXT="no, am working to improve this quickly. see proposal"/>
</node>
</node>
<node CREATED="1550056904263" ID="ID_1120995547" MODIFIED="1550056911793" POSITION="left" TEXT="Project Overview">
<node CREATED="1550056912488" ID="ID_308878542" MODIFIED="1550056914934" TEXT="Problem">
<node CREATED="1550763610818" ID="ID_1578053944" MODIFIED="1550763713968" TEXT="deep learning can take in data to produce a prediction of where an item may be in space relative to the sensors, but for autonomous driving, is there a way to reduce the number of sensors used, and can good results still be achieved?"/>
</node>
<node CREATED="1550056915487" ID="ID_612912837" MODIFIED="1550056917071" TEXT="Objective">
<node COLOR="#ff0000" CREATED="1550763718090" ID="ID_1449885495" MODIFIED="1550763755645" TEXT="compare two sensor setups together to see which performs better, and by how much. compare a single RGB camera vs two RGB stereo cameras"/>
</node>
<node CREATED="1550056917510" ID="ID_565419984" MODIFIED="1550056921090" TEXT="Hypothesis">
<node COLOR="#ff0000" CREATED="1550763760473" ID="ID_1995876075" MODIFIED="1550763778876" TEXT="stereo vision cameras will perform better, but not sure by how much."/>
</node>
<node CREATED="1550056923039" ID="ID_1435257805" MODIFIED="1550056930807" TEXT="General Procedure">
<node CREATED="1550763780963" ID="ID_1977590322" MODIFIED="1550763836091" TEXT="1. take a dataset that has both RGB and stereo images"/>
<node CREATED="1550763822482" ID="ID_1189320144" MODIFIED="1550763822484" TEXT="2. develop two networks that learn to generate 3D pose proposals of pedestrians or cars"/>
<node CREATED="1550763838805" ID="ID_87269393" MODIFIED="1550763875631" TEXT="3. evaluate each network on its ability to create a 3D bounding box (x,y,z,h,w,d) of where the desired class is. "/>
<node CREATED="1550763876427" ID="ID_822295650" MODIFIED="1550763879639" TEXT="compare the results"/>
</node>
<node CREATED="1550763884407" ID="ID_937189561" MODIFIED="1550763889476" TEXT="required literature search">
<node CREATED="1550763890254" ID="ID_226663849" MODIFIED="1550763898151" TEXT="single-camera 3D bounding box estimation"/>
<node CREATED="1550763898448" ID="ID_1619942799" MODIFIED="1550763904691" TEXT="stereo camrea 3D bounding box estimation"/>
<node CREATED="1550763904983" ID="ID_775280810" MODIFIED="1550763919415" TEXT="datasets that have stereo images in outdoor (preferably) scenes"/>
</node>
</node>
</node>
</map>
