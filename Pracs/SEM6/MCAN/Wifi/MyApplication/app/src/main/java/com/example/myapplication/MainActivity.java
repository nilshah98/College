package com.example.myapplication;

import android.content.Context;
import android.content.Intent;
import android.net.wifi.WifiManager;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Calendar;
import java.util.Date;

public class MainActivity extends AppCompatActivity {
    public static final String EXTRA_MESSAGE = "com.example.myfirstapp.MESSAGE";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void sendMessage(View view){
        Intent intent = new Intent(this, DisplayMessageActivity.class);
        String message = disp();
        intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);
    }

    private String disp(){
        WifiManager wifiManager = (WifiManager) this.getApplicationContext().getSystemService(Context.WIFI_SERVICE);
        int rssi = wifiManager.getConnectionInfo().getRssi();
        int level = WifiManager.calculateSignalLevel(rssi,5);
        String ssid = wifiManager.getConnectionInfo().getSSID();
        String MacAddr = wifiManager.getConnectionInfo().getMacAddress();

        String message = ("\t\tSignal Strength of "+ ssid+"\n\n\t\tMac Address = "+ MacAddr+"\n\n\t\tRSSI = "+ rssi + " dbm \n\n\t\tLevel = "+ level + " out of 5");

        return message;
    }
    public void savetofile(View view){

        File directory = new File(Environment.getExternalStorageDirectory() + java.io.File.separator +"Wifi-Data");
        Toast.makeText(this, directory.toString(), Toast.LENGTH_SHORT).show();
        if (!directory.exists())
            Toast.makeText(this, (directory.mkdirs() ? "Directory has been created" : "Directory not created"), Toast.LENGTH_SHORT).show();
        else
            Toast.makeText(this, "File Updated", Toast.LENGTH_SHORT).show();
        System.out.println(directory);
        File file = new File(Environment.getExternalStorageDirectory() + java.io.File.separator +"Wifi-Data" + java.io.File.separator + "Wifi-Data.txt");
        System.out.println(file);

        Date currentTime = Calendar.getInstance().getTime();
        if(!file.exists()) {
            try {
                file.createNewFile();
            } catch (Exception e) {
                Toast.makeText(MainActivity.this,e.getMessage(),Toast.LENGTH_SHORT).show();
            }
        }

        try {
            OutputStreamWriter file_writer = new OutputStreamWriter(new FileOutputStream(file,true));
            BufferedWriter buffered_writer = new BufferedWriter(file_writer);
            buffered_writer.write("############\n"+currentTime+"\n"+disp().toString()+"\n");
            buffered_writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
