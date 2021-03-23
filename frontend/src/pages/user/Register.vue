<template>

  <div>
    <div class="absolute-center" style="margin-top: -3rem">
      <div class="row justify-center">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor"
        style="height: 4rem">
          <path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd" />
        </svg>
      </div>
      <div class="row justify-center" style="margin-top: 0.1rem">
        <div class="col-12">
          <h4 style="font-size: 24px; text-align: center; font-weight: bolder">
            Create your account
          </h4>
        </div>
      </div>
      <div class="row" style="width: 320px;">
        <RegisterForm/>
      </div>
      <div class="row" style="margin-top: 1rem; margin-bottom: -4rem">
        <div class="col-12 text-center">
          <p class="">or</p>
        </div>
        <div class="col-12 text-center" style="margin-bottom: 1rem">
          <router-link :to="{name: 'Login'}" class="animate-pulse text-amber-6 text-center">login</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RegisterForm from "components/user/forms/RegisterForm";
export default {
  name: "Register",
  components: {RegisterForm}
}
</script>

<style scoped>
.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  text-decoration: none;
}
@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: .5;
  }

}
</style>
