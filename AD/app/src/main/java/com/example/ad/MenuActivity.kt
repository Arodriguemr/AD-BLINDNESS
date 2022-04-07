package com.example.ad

import android.graphics.ColorFilter
import android.graphics.ColorMatrixColorFilter
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.SeekBar
import android.widget.ImageView
import androidx.appcompat.app.ActionBar
import com.example.ad.databinding.ActivityMenuBinding
import com.google.firebase.auth.FirebaseAuth

class MenuActivity : AppCompatActivity() {

    //ImageView
    private lateinit var imageView: ImageView

    //SeekBar
    private lateinit var redBar: SeekBar
    private lateinit var greenBar: SeekBar
    private lateinit var blueBar: SeekBar

    //ViewBinding
    private lateinit var binding: ActivityMenuBinding

    //ActionBar
    private lateinit var actionBar: ActionBar

    //FirebaseAuth
    private lateinit var firebaseAuth: FirebaseAuth


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMenuBinding.inflate(layoutInflater)
        setContentView(binding.root)

        //init firebase auth
        firebaseAuth = FirebaseAuth.getInstance()
        checkUser()

        //Handle click, logout
        binding.logoutBtn.setOnClickListener {
            firebaseAuth.signOut()
            checkUser()
        }

        imageView = findViewById(binding.image.id)

        redBar = findViewById(binding.red.id)
        greenBar = findViewById(binding.green.id)
        blueBar = findViewById(binding.blue.id)

    }


    private fun checkUser() {
       //Check user is logged in or not
        val firebaseUser = firebaseAuth.currentUser
        if (firebaseUser != null){
            //User not null, user is logged in
            val email = firebaseUser.email
            //Set to text view
            binding.emailTv.text = email
        }
        else {
            //User is null, user is no logged
            startActivity(Intent(this, LoginActivity::class.java))
            finish()
        }
    }
}