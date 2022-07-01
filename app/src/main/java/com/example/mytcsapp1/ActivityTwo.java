package com.example.mytcsapp1;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;

public class ActivityTwo extends Activity {

    // Defining the object for button
    Button button1;
    @Override
    public void onCreate(Bundle bundle)
    {
        super.onCreate(bundle);
        setContentView(R.layout.activity_two);

        // Bind the components to their respective objects
        // by assigning their IDs
        // with the help of findViewById() method
        //For inserting error.
        button1 = (Button)findViewById(R.id.Button01);

        button1.setOnClickListener(new OnClickListener() {
         public void onClick(View view)
         {

        // Creating explicit intent
        Intent i = new Intent(getApplicationContext(),
               MainActivity3.class);
        startActivity(i);
        }
        });
    }
}