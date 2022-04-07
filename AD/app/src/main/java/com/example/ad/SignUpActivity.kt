package com.example.ad

import android.app.ProgressDialog
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.TextUtils
import android.util.Patterns
import android.widget.Toast
import androidx.appcompat.app.ActionBar
import com.example.ad.databinding.ActivitySignUpBinding
import com.google.firebase.auth.FirebaseAuth

class SignUpActivity : AppCompatActivity() {
    //ViewBinding
    private lateinit var binding: ActivitySignUpBinding

    //ActionBar
    private lateinit var  actionBar: ActionBar

    //ProgressDialog
    private lateinit var progressDialog: ProgressDialog

    //FirebaseAuth
    private  lateinit var firebaseAuth: FirebaseAuth
    private  var email = ""
    private  var password = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySignUpBinding.inflate(layoutInflater)
        setContentView(binding.root)

        //Configure progress dialog
        progressDialog = ProgressDialog(this)
        progressDialog.setTitle("Please wait")
        progressDialog.setMessage("Creating account in...")
        progressDialog.setCanceledOnTouchOutside(false)

        //Init firebase auth
        firebaseAuth = FirebaseAuth.getInstance()

        //Handle click, begin signups
        binding.signUpBtn.setOnClickListener {
            //Validate data
            validateData()
        }

        //handle click, open register activity
        binding.haveAccountTv.setOnClickListener{
            startActivity(Intent(this, LoginActivity::class.java))
        }

    }

    private fun validateData() {
        //Get data
        email = binding.emailEt.text.toString().trim()
        password = binding.passwordEt.text.toString().trim()

        //validate data
        if (!Patterns.EMAIL_ADDRESS.matcher(email).matches()){
            //Invalid email format
            binding.emailEt.error = "Invalid email format"
        }
        else if (TextUtils.isEmpty(password)){
            //Password isn't entered
            binding.passwordEt.error = "Please enter password"
        }
        else if (password.length < 6){
            //Password length is less than 6
            binding.passwordEt.error = "Password must atleast 6 chracters long"
        }
        else{
            firebaseSignUp()
        }
    }

    private fun firebaseSignUp() {
        //Show progress
        progressDialog.show()

        //Create account
        firebaseAuth.createUserWithEmailAndPassword(email, password)
            .addOnSuccessListener {
                //SignUp success
                progressDialog.dismiss()
                //get current user
                val firebaseUser = firebaseAuth.currentUser
                val email = firebaseUser!!.email
                Toast.makeText(this, "Account created with email $email", Toast.LENGTH_SHORT).show()

                //Open profile
                startActivity(Intent(this, MenuActivity::class.java))
                finish()
            }
            .addOnFailureListener { e ->
                //SignUp failed
                progressDialog.dismiss()
                Toast.makeText(this, "SignUp failed due to ${e.message}", Toast.LENGTH_SHORT).show()
            }
    }

    override fun onSupportNavigateUp(): Boolean {
        onBackPressed() //Go back previous activity, when back button of actionbar clicked
        return super.onSupportNavigateUp()
    }
}